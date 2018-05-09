# Text viewer
import curses


class LineBufferNode:
    def __init__(self, line=""):
        self.line = line
        self.next = -1
        self.prev = -1


class TextFileViewer:
    def __init__(self):
        self.head = LineBufferNode()
        self.tail = LineBufferNode()

        self.head.next = self.tail
        self.head.prev = self.head
        self.tail.next = self.tail
        self.tail.prev = self.head

        self.total_line_num = 0
        self.stdscr = curses.initscr()

    def load_file(self, file_name):
        fd = open(file_name, 'r')
        self.file_name = file_name
        self.total_line_num = 0

        print("File loading...")
        while (True):
            line_buffer = fd.readline()
            if not line_buffer:
                break

            new_line_buffer_node = LineBufferNode(line_buffer)
            new_line_buffer_node.prev = self.tail.prev
            new_line_buffer_node.next = self.tail
            self.tail.prev.next = new_line_buffer_node
            self.tail.prev = new_line_buffer_node

            self.total_line_num += 1

        fd.close()

    def show_header(self):
        string = " Text Viewer : " + self.file_name
        self.stdscr.addstr(0, 0, string, curses.A_REVERSE)
        self.stdscr.refresh()

    def show_page(self, line_node):
        # Clear screen
        self.stdscr.clear()
        # Show header
        self.show_header()

        line_num = 1
        # Can show total 29 lines (1 line for header and 28 lines for context
        while line_node != self.tail:
            try:
                self.stdscr.addstr(line_num, 0, line_node.line)
            except:
                break

            line_node = line_node.next
            line_num += 1

        self.stdscr.refresh()

        return line_num

    def move_line(self, line_num, line_node):

        self.stdscr.addstr(1, 0, str(line_num))

        if line_num < 0:
            while line_num != 0 and line_node.prev != self.head:
                line_node = line_node.prev
                line_num += 1
        else:
            while line_num != 0 and line_node.next != self.tail:
                line_node = line_node.next
                line_num -= 1

        return line_node

    def key_proc(self):
        curses.noecho()
        self.stdscr.keypad(1)

        line_node = self.head.next
        line_num = self.show_page(line_node)

        while True:
            key = self.stdscr.getch()
            if key == curses.KEY_PPAGE: # Page Up
                line_node = self.move_line(-1*line_num, line_node)
                self.show_page(line_node)
            if key == curses.KEY_NPAGE: # Page Down
                line_node = self.move_line(line_num, line_node)
                self.show_page(line_node)
            if key == ord('q') or key == ord('Q'):
                break
            self.stdscr.refresh()

# main() function
if __name__ == "__main__":
    # Get file name to read
    file_name = input("Please input file name to load -> ")

    # Initialize TextFileViewer class
    text_viewer = TextFileViewer()
    # Read file
    text_viewer.load_file(file_name)
    # Handle key input
    text_viewer.key_proc()
