const std = @import("std");

const debug = std.debug;
const assert = debug.assert;
const testing = std.testing;

const mem = std.mem;
const Allocator = mem.Allocator;

pub fn Document(comptime Attributes: type) type {
    return struct {
        const Self = @This();
        text: std.ArrayList(u8),
        attributes: ?Attributes,

        /// Initialise the document
        pub fn init(allocator: Allocator) Document(Attributes) {
            return .{
                .text = std.ArrayList(u8).init(allocator),
                .attributes = null,
            };
        }

        /// Deinitialise the Document and free memory
        pub fn deinit(self: Self) void {
            self.text.deinit();
        }
    };
}

// Will create new structs for documents with attributes like author, source, title
// Documents return a type, so that individual fields can be added to capture structured info (e.g. a salary field for a job description)
// Documents can be created from files (and create all in a directory)
// Some functioanlity to ensure not duplicate documents are created?
// Documents will own all their content, so other analyses can slices instead of duplicating strings
// That will mean to rewrite some of the content analysis section

test "create document from string" {
    const a = testing.allocator;

    var doc = Document(void).init(a);
    defer doc.deinit();

    const text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";

    try doc.text.appendSlice(text);
    try testing.expectEqual(doc.text.items[0], 'L');
}
