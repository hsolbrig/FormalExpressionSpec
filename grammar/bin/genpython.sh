# Note: there is an error in the antlr code generator that puts it in the directory *above* the target -- thus the ".empty"
#       which must exist.
java -jar /usr/local/lib/antlr-4.5-complete.jar -Dlanguage=Python3 -o ../../implementation/ECLparser/parser/.empty -no-listener -visitor ../ECL.g4
