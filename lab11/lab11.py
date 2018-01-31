import LSystem

def main():
	filelist = ["hilbertcurve.txt", "dragoncurve.txt", "arrowheadcurve.txt", "peanogospercurve.txt", "sierpinskitrianglecurve.txt"]
	for i in filelist:
		print("Curve: ", i)
		sys = LSystem.LSystem(i)
		sys.drawCurve()
main()
