const std = @import("std");

const debug = std.debug;
const assert = debug.assert;
const testing = std.testing;

const mem = std.mem;
const Allocator = mem.Allocator;

pub const Options = struct { split: []const u8 = " " };

pub const ContentAnalysis = struct {
    allocator: Allocator,
    items: std.StringHashMap(u32),
    options: Options,

    /// Initialise an empty Content Analysis
    pub fn init(allocator: Allocator) ContentAnalysis {
        return ContentAnalysis{
            .allocator = allocator,
            .items = std.StringHashMap(u32).init(allocator),
            .options = Options{},
        };
    }

    /// Deinitialise and free memory
    pub fn deinit(self: *ContentAnalysis) void {
        var iter = self.items.iterator();
        while (iter.next()) |entry| {
            self.allocator.free(entry.key_ptr.*);
        }
        self.items.deinit();
    }

    /// Adds a provided phrase or word to the Content Analysis
    pub fn countword(self: *ContentAnalysis, word: []const u8) !void {
        // Create an owned string of the provided word or phrase
        const key = try self.allocator.dupe(u8, word);

        // Check if the word or pharse is already in the hashmap, add if not found already
        const found = try self.items.getOrPut(key);
        if (found.found_existing) {
            // If pre-existing, increment count by 1 and free the owned string
            found.value_ptr.* += 1;
            self.allocator.free(key);
        } else {
            // If newlty added, set its counter to 1
            found.value_ptr.* = 1;
        }
    }

    /// Count words and phrases in a provided string
    pub fn countwords(self: *ContentAnalysis, string: []const u8) !void {
        var words = std.mem.splitAny(u8, string, self.options.split);
        while (words.next()) |word| {
            try self.countword(word);
        }
    }

    /// Return the counted frequency of a word or null if word not found
    pub fn getcount(self: ContentAnalysis, word: []const u8) ?u32 {
        return self.items.get(word);
    }

    /// Need a function to get the wordcount by key
    pub fn wordscounted(self: ContentAnalysis) u32 {
        return self.items.count();
    }

    /// Return an iterator containing all counted words
    pub fn countedwords(self: ContentAnalysis) u32 {
        return self.items.keyIterator();
    }
};

/// Function to compare the which string has been counted most
fn compare(_: void, a: std.StringHashMap(u32).Entry, b: std.StringHashMap(u32).Entry) bool {
    return a.value_ptr.* > b.value_ptr.*;
}

test "fixed - text - Lorem ipsum" {
    const a = testing.allocator;

    var WCount = ContentAnalysis.init(a);
    defer WCount.deinit();

    const text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
    try WCount.countwords(text);

    try testing.expectEqual(WCount.getcount("Lorem"), 1);
    try testing.expectEqual(WCount.getcount("in"), 3);
    try testing.expectEqual(WCount.getcount("NotInThere"), null);
}
