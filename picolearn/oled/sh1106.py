from micropython import const
import framebuf

# SH1106 command constants
_SH1106_SET_CONTRAST = const(0x81)
_SH1106_DISPLAY_ALL_ON_RESUME = const(0xA4)
_SH1106_DISPLAY_ALL_ON = const(0xA5)
_SH1106_NORMAL_DISPLAY = const(0xA6)
_SH1106_INVERT_DISPLAY = const(0xA7)
_SH1106_DISPLAY_OFF = const(0xAE)
_SH1106_DISPLAY_ON = const(0xAF)
_SH1106_SET_DISPLAY_OFFSET = const(0xD3)
_SH1106_SET_COM_PINS = const(0xDA)
_SH1106_SET_VCOM_DETECT = const(0xDB)
_SH1106_SET_DISPLAY_CLOCK_DIV = const(0xD5)
_SH1106_SET_PRECHARGE = const(0xD9)
_SH1106_SET_MULTIPLEX = const(0xA8)
_SH1106_SET_LOW_COLUMN = const(0x00)
_SH1106_SET_HIGH_COLUMN = const(0x10)
_SH1106_SET_START_LINE = const(0x40)
_SH1106_MEMORY_MODE = const(0x20)
_SH1106_COLUMN_ADDR = const(0x21)
_SH1106_PAGE_ADDR = const(0x22)
_SH1106_COM_SCAN_INC = const(0xC0)
_SH1106_COM_SCAN_DEC = const(0xC8)
_SH1106_SEG_REMAP = const(0xA0)
_SH1106_CHARGE_PUMP = const(0x8D)

class SH1106_I2C(framebuf.FrameBuffer):
    def __init__(self, width, height, i2c, addr=0x3c):
        self.width = width
        self.height = height
        self.i2c = i2c
        self.addr = addr
        self.pages = self.height // 8
        self.buffer = bytearray(self.width * self.pages)
        super().__init__(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.init_display()

    def init_display(self):
        cmds = [
            _SH1106_DISPLAY_OFF,
            _SH1106_SET_DISPLAY_CLOCK_DIV, 0x80,
            _SH1106_SET_MULTIPLEX, self.height - 1,
            _SH1106_SET_DISPLAY_OFFSET, 0x00,
            _SH1106_SET_START_LINE | 0x00,
            _SH1106_CHARGE_PUMP, 0x14,
            _SH1106_MEMORY_MODE, 0x00,
            _SH1106_SEG_REMAP | 0x01,
            _SH1106_COM_SCAN_DEC,
            _SH1106_SET_COM_PINS, 0x12,
            _SH1106_SET_CONTRAST, 0xCF,
            _SH1106_SET_PRECHARGE, 0xF1,
            _SH1106_SET_VCOM_DETECT, 0x40,
            _SH1106_DISPLAY_ALL_ON_RESUME,
            _SH1106_NORMAL_DISPLAY,
            _SH1106_DISPLAY_ON
        ]
        for cmd in cmds:
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def write_cmd(self, cmd):
        self.i2c.writeto(self.addr, b'\x00' + bytearray([cmd]))

    def show(self):
        for page in range(self.pages):
            self.write_cmd(0xB0 + page)
            self.write_cmd(_SH1106_SET_LOW_COLUMN | 2)
            self.write_cmd(_SH1106_SET_HIGH_COLUMN | 0)
            start = self.width * page
            end = start + self.width
            self.i2c.writeto(self.addr, b'\x40' + self.buffer[start:end])

    def poweroff(self):
        self.write_cmd(_SH1106_DISPLAY_OFF)  # Turn off display
        self.fill(0)                         # Clear buffer
        self.show()                         # Refresh screen (now blank)
