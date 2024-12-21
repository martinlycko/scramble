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
            var iter = self.items.iterator();
            while (iter.next()) |entry| {
                self.allocator.free(entry.key_ptr.*);
            }
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
            const key = try self.allocator.dupe(u8, word);
            const found = try self.items.getOrPut(key);
            if (found.found_existing) {
                found.value_ptr.* += 1;
                self.allocator.free(key);
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

        /// Return an iterator containing all counted words
        pub fn countedwords(self: *Self) u32 {
            return self.items.keyIterator();
        }

        /// Print all counted words from most to least counted
        pub fn printorderedwordlist(self: *Self) !void {
            const words_slice = try self.allocator.alloc(std.StringHashMap(u32).Entry, self.wordscounted());
            defer self.allocator.free(words_slice);

            var i: usize = 0;
            var it = self.items.iterator();
            while (it.next()) |entry| : (i += 1) {
                words_slice[i] = entry;
            }
            std.sort.insertion(std.StringHashMap(u32).Entry, words_slice, {}, compare);

            var stdout = std.io.bufferedWriter(std.io.getStdOut().writer());
            for (words_slice) |entry| {
                try stdout.writer().print("{s} {d}\n", .{ entry.key_ptr.*, entry.value_ptr.* });
            }
            try stdout.flush();
        }
    };
}

/// Function to compare the which string has been counted most
fn compare(_: void, a: std.StringHashMap(u32).Entry, b: std.StringHashMap(u32).Entry) bool {
    return a.value_ptr.* > b.value_ptr.*;
}

test "fixed - text - Lorem ipsum" {
    const a = testing.allocator;

    var WCount = WordCounter().init(a);
    defer WCount.deinit();

    const text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
    try WCount.countwords(text);

    try testing.expectEqual(WCount.getcount("Lorem"), 1);
    try testing.expectEqual(WCount.getcount("in"), 3);
    try testing.expectEqual(WCount.getcount("NotInThere"), null);
}

test "fixed - text - test 3x" {
    const a = testing.allocator;

    var WCount = WordCounter().init(a);
    defer WCount.deinit();

    const text = "test test test";
    try WCount.countwords(text);

    try testing.expectEqual(WCount.wordscounted(), 1);
    try testing.expectEqual(WCount.getcount("test"), 3);
}

test "fixed - text - test 3x3" {
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

test "fixed - word - test 3x" {
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

test "fixed - word - test 3x3" {
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

test "file - text - Lorem ipsum" {
    const a = testing.allocator;

    var dir = try std.fs.cwd().openDir("data", .{});
    defer dir.close();

    var file = try dir.openFile("test-data1.txt", .{});
    defer file.close();

    const content = try file.readToEndAlloc(a, 10000);
    defer a.free(content);

    var WCount = WordCounter().init(a);
    defer WCount.deinit();

    try WCount.countwords(content);

    try testing.expectEqual(WCount.getcount("Lorem"), 1);
    try testing.expectEqual(WCount.getcount("in"), 3);
    try testing.expectEqual(WCount.getcount("NotInThere"), null);
}

test "file - text - Lorem ipsum 2x" {
    const a = testing.allocator;

    var dir = try std.fs.cwd().openDir("data", .{});
    defer dir.close();

    var file = try dir.openFile("test-data1.txt", .{});
    defer file.close();

    const content = try file.readToEndAlloc(a, 10000);
    defer a.free(content);

    var WCount = WordCounter().init(a);
    defer WCount.deinit();

    try WCount.countwords(content);
    try WCount.countwords(content);

    try testing.expectEqual(WCount.getcount("Lorem"), 2);
    try testing.expectEqual(WCount.getcount("in"), 6);
    try testing.expectEqual(WCount.getcount("NotInThere"), null);

    //try WCount.printorderedwordlist();
}

test "iterate over files in directory" {
    const a = testing.allocator;

    var WCount = WordCounter().init(a);
    defer WCount.deinit();

    var dir = try std.fs.cwd().openDir("data", .{ .iterate = true });
    defer dir.close();

    var iter = dir.iterate();
    while (try iter.next()) |entry| {
        if (entry.kind == .file) {
            //std.debug.print("{s} \n", .{entry.name});
            var file = try dir.openFile(entry.name, .{});
            defer file.close();

            const content = try file.readToEndAlloc(a, 100000);
            defer a.free(content);

            try WCount.countwords(content);
        }
    }

    try testing.expectEqual(WCount.getcount("Lorem"), 2);
    try testing.expectEqual(WCount.getcount("in"), 6);
    try testing.expectEqual(WCount.getcount("NotInThere"), null);
}
