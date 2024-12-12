const std = @import("std");

const debug = std.debug;
const assert = debug.assert;
const testing = std.testing;

const mem = std.mem;
const Allocator = mem.Allocator;

pub fn WordCounter() type {
    return struct {
        const Self = @This();
        allocator: Allocator,
        items: std.StringHashMap(u32),

        /// Initialise the hash map and set the allocator
        pub fn init(allocator: Allocator) Self {
            return Self{
                .allocator = allocator,
                .items = std.StringHashMap(u32).init(allocator),
            };
        }

        /// Deinitialise the WordCounter and free memory
        pub fn deinit(self: *Self) void {
            self.items.deinit();
        }

        /// Count words in a provided string
        pub fn countwords(self: *Self, string: []const u8) !void {
            var words = std.mem.split(u8, string, " ");
            while (words.next()) |word| {
                try self.countword(word);
            }
        }

        /// Adds a provided word
        pub fn countword(self: *Self, word: []const u8) !void {
            const found = try self.items.getOrPut(word);
            if (found.found_existing) {
                found.value_ptr.* += 1;
            } else {
                found.value_ptr.* = 1;
            }
        }

        /// Return the counted frequency of a word or null if word not found
        pub fn getcount(self: *Self, word: []const u8) ?u32 {
            return self.items.get(word);
        }

        /// Need a function to get the wordcount by key
        pub fn wordscounted(self: *Self) u32 {
            return self.items.count();
        }
    };
}

test "text - Lorem ipsum" {
    const a = testing.allocator;

    var WCount = WordCounter().init(a);
    defer WCount.deinit();

    const text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
    try WCount.countwords(text);

    try testing.expectEqual(WCount.getcount("Lorem"), 1);
    try testing.expectEqual(WCount.getcount("in"), 3);
    // try testing.expectEqual(WCount.getcount("In"), 3);
    try testing.expectEqual(WCount.getcount("NotInThere"), null);
}

test "text - test 3x" {
    const a = testing.allocator;

    var WCount = WordCounter().init(a);
    defer WCount.deinit();

    const text = "test test test";
    try WCount.countwords(text);

    try testing.expectEqual(WCount.wordscounted(), 1);
    try testing.expectEqual(WCount.getcount("test"), 3);
}

test "text - test 3x3" {
    const a = testing.allocator;

    var WCount = WordCounter().init(a);
    defer WCount.deinit();

    const text = "test1 test2 test3";
    try WCount.countwords(text);

    try testing.expectEqual(WCount.wordscounted(), 3);
    try testing.expectEqual(WCount.getcount("test1"), 1);
    try testing.expectEqual(WCount.getcount("test2"), 1);
    try testing.expectEqual(WCount.getcount("test3"), 1);
}

test "word - test 3x" {
    const a = testing.allocator;

    var WCount = WordCounter().init(a);
    defer WCount.deinit();

    const word = "test";
    try WCount.countword(word);
    try WCount.countword(word);
    try WCount.countword(word);

    try testing.expectEqual(WCount.wordscounted(), 1);
    try testing.expectEqual(WCount.getcount("test"), 3);
}

test "word - test 3x3" {
    const a = testing.allocator;

    var WCount = WordCounter().init(a);
    defer WCount.deinit();

    try WCount.countword("test1");
    try WCount.countword("test2");
    try WCount.countword("test3");

    try testing.expectEqual(WCount.wordscounted(), 3);
    try testing.expectEqual(WCount.getcount("test1"), 1);
    try testing.expectEqual(WCount.getcount("test2"), 1);
    try testing.expectEqual(WCount.getcount("test3"), 1);
}
