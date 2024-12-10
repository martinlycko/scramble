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

        /// Count words in a provided string
        pub fn count(self: *Self, string: []const u8) !void {
            var words = std.mem.split(u8, string, " ");
            while (words.next()) |word| {
                const found = try self.items.getOrPut(word);
                if (found.found_existing) {
                    found.value_ptr.* += 1;
                } else {
                    found.value_ptr.* = 1;
                }
            }
        }
    };
}

test "basic" {
    const a = testing.allocator;

    var WCount = WordCounter().init(a);
    defer WCount.items.deinit();

    const text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";

    try WCount.count(text);
    std.debug.print("{}", .{WCount.items.count()});
}
