import collections
from winsound import Beep

Pch = collections.namedtuple('PCH', ['octave', 'pitch'])


def welcomeMessage():
	print "Hello."
	print "This program will convert octave/pitchclass pairs into their respective frequency."


def inputFunc():
	octave = int(raw_input("Input an octave: "))
	pitchclass = int(raw_input("Input a pitch class: "))

	return Pch(octave, pitchclass)


def freqMath(pch):
	frequency = pch.octave - 9
	frequency = float(frequency) / 12
	pitchval = pch.pitch - 4
	frequency += pitchval
	frequency = 2 ** frequency
	return frequency * 440


def playSound(frequency):
	if frequency < 38:
		frequency = 38
		print "Warning, the frequency is less than 37 Hz, automatically scaling up to 37 Hz"
	if frequency > 32767:
		frequency = 32767
		print "Warning, the frequency is more than 32767 Hz, automatically scaling down to 32767 Hz"
	Beep(int(frequency), 1500)


def main():
	welcomeMessage()
	pchCombo = inputFunc()
	frequency = freqMath(pchCombo)
	print "The combination " + str(pchCombo.pitch) + "." + str(pchCombo.octave) + " produces this hertz %s " % frequency
	playSound(frequency)
	raw_input("Press enter key to continue")


def tryAgain():
	print "Would you like to restart?"
	boolval = raw_input(">>> ")
	tryer = False
	if 'y' in boolval:
		tryer = True
	else:
		tryer = False
	return tryer


main()
while not tryAgain:
	main()

