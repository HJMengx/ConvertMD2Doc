import pypandoc
import sys

if __name__ == "__main__":
	if len(sys.argv) > 2:
		print("你输入了过多的参数, 后面的参数将被忽略")
	inputFile = sys.argv[1]

	output = pypandoc.convert(source=inputFile, format='html', to='docx', outputfile="output.docx", extra_args=['-RTS'])