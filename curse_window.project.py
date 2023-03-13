#!/opt/homebrew/bin/python3.11
import sys
import time
import curses as cs
import subprocess as sp
from curses import wrapper
from datetime import date

#	  ___/=| COLORS |=\___
#	 |/------------------\|
#	 || COLOR_BLACK:   0 ||
#	 ||	COLOR_RED:	   1 ||
#	 ||	COLOR_GREEN:   2 ||
#	 ||	COLOR_YELLOW:  3 ||
#	 ||	COLOR_BLUE:    4 ||
#	 ||	COLOR_MAGENTA: 5 ||
#	 ||	COLOR_CYAN:    6 ||
#	 ||	COLOR_WHITE:   7 ||
#	 |\==================/|

returnNumber = 0;

def main(args):

	try:
		stdscr = cs.initscr()
		cs.noecho() # turn off automatic echoing of keys to the screen
		cs.cbreak() # react to keys instantly
		cs.curs_set(0)
		cs.start_color()
		cs.use_default_colors()
		cs.init_pair(1, 1, 0)
		cs.init_pair(2, 2, 7)
		cs.init_pair(3, 3, 2)
		cs.init_pair(4, 4, 7)
		cs.init_pair(5, 5, 7)
		cs.init_pair(6, 6, 0)
		cs.init_pair(7, 7, 2)
		cs.init_pair(8, cs.COLOR_RED, cs.COLOR_WHITE)
		cs.init_pair(9, cs.COLOR_CYAN, cs.COLOR_BLACK)
		cs.init_pair(10, cs.COLOR_YELLOW, cs.COLOR_MAGENTA)
		cs.init_pair(11, cs.COLOR_WHITE, cs.COLOR_BLUE)
		cs.init_pair(12, cs.COLOR_WHITE, cs.COLOR_MAGENTA)
		cs.init_pair(13, cs.COLOR_YELLOW, cs.COLOR_GREEN)
		cs.init_pair(14, cs.COLOR_WHITE, cs.COLOR_GREEN)
	except Exception as _ex:
		returnNumber = 301
		throwEx(301, _ex);

	try:
		while True:
			c = stdscr.getch()
#			1
			if c == ord("1"):
				stdscr.addstr(1, 0, "\n\r\tThis is a 1's number one string.", cs.color_pair(8));
#			2
			elif c == ord("2"):
				stdscr.addstr(2, 0, "\n\r\tThis is a 2's number two string.", cs.color_pair(9));
#			3
			elif c == ord("3"):
				stdscr.addstr(3, 0, "\n\r\tThis is a 3's number three string.", cs.color_pair(10));
#			4
			elif c == ord("4"):
				stdscr.addstr(4, 0, "\n\r\tThis is a 4's number four  string.", cs.color_pair(11));
#			5
			elif c == ord("5"):
				stdscr.addstr(5, 0, "\n\r\tThis is a 5's number five string.", cs.color_pair(12));
#			6
			elif c == ord("6"):
				stdscr.addstr(6, 0, "\nThis is a 6's number six string!", cs.color_pair(6));
#			7
			elif c == ord("7"):
				readin_table(stdscr);
#			8
			elif c == ord("8"):
				draw_window(stdscr);
#			c
			elif c == ord("c"):
				stdscr.clear();
#			q
			elif c == ord("q"):
				break;
	except Exception as _ex:
		returnNumber=302;
		throwEx(302, _ex);

# 7
def readin_table(stdscr):
	try:
		today=date.today()
		str0="\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557";
		str1="\u2551 t's   \u2551 number seven string!   \u2551";
		str2="\u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256C\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563";
		str3="\u2551 {1} \u2551  {0} \u2551 {2} \u2551".format( today.strftime("%d/%m/%Y"), time.strftime("%H:%M"), today.strftime("%B") );
		str4="\u255A\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255D";

		stdscr.addstr(0, 0, "{0}\n\r{1}\n\r{2}\n\r{3}\n\r{4}".format(str0, str1, str2, str3, str4), cs.color_pair(13));
		stdscr.refresh();
	except Exception as _ex:
		returnNumber=303;
		throwEx(303, _ex);

# 8
def draw_window(stdscr):
	try:
		win = cs.newwin(0, 0, 8, 57);
		win.addstr(0, 0, "|====> Pair 1::0 <===|===> [RED] <========|", cs.color_pair(1))
		win.addstr(1, 0, "|====> Pair 2::7 <===|===> [GREEN] <======|", cs.color_pair(2))
		win.addstr(2, 0, "|====> Pair 3::2 <===|===> [YELLOW] <=====|", cs.color_pair(3))
		win.addstr(3, 0, "|====> Pair 4::7 <===|===> [BLUE] <=======|", cs.color_pair(4))
		win.addstr(4, 0, "|====> Pair 5::7 <===|===> [MAGENTA] <====|", cs.color_pair(5))
		win.addstr(5, 0, "|====> Pair 6::0 <===|===> [CYAN] <=======|", cs.color_pair(6))
		win.addstr(6, 0, "|====> Pair 7::2 <==|===> [WHITE] <======|", cs.color_pair(7))
		win.addstr(8, 0, " ___/=| COLORS |=\____ \n\r\
|/-------------------\|\n\r\
||  COLOR_BLACK:   0 ||\n\r\
||  COLOR_RED:     1 ||\n\r\
||  COLOR_GREEN:   2 ||\n\r\
||  COLOR_YELLOW:  3 ||\n\r\
||  COLOR_BLUE:    4 ||\n\r\
||  COLOR_MAGENTA: 5 ||\n\r\
||  COLOR_CYAN:    6 ||\n\r\
||  COLOR_WHITE:   7 ||\n\r\
|\===================/|", cs.color_pair(14))
		win.refresh()
		stdscr.refresh()
	except Exception as ex:
		returnNumber=304;
		throwEx(304, _ex);

def throwEx(_rn, _ex):
	_traceBack = sys.exc_info()
	print(Fore.RED + "______________________| THROWING EXCEPTION |______________________\n" + Fore.WHITE + str(_traceBack) + "\nException:\n" + Fore.Blue +  str(_ex) + Style.RESET_ALL + "\n\r");
	returnNumber = _rn;

def terminateApp(_rn):
	try:
		cs.nocbreak();
		cs.echo();
		cs.curs_set(False);
		cs.endwin();
#		sp.run(["\e[0;37m"]);
		print("Terminating...\n\rPlease be patient at this time.\n\rThank You.\n\r");
#		sp.run(["\e[0;m"]);
		sys.exit(_rn);
	except Exception as _ex:
		throwEx(306,  _ex);

# Call Main Function..
if __name__ == "__main__":
	try:
		wrapper(main(sys.argv));
	except KeyboardInterrupt:
		print("[CNTRL] + C - Keyboard Interupt terminating application.")
	except Exception as _ex:
		throwEx(300, _ex);
	finally:
		terminateApp(returnNumber);
