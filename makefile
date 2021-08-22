objects = example/hello.o example/factorial.o example/main.o
hello : $(objects)
		g++ -o hello $(objects)

factorial.o : example/factorial.cpp example/functions.h

main.o : example/main.cpp example/functions.h

hello.o : example/hello.cpp example/functions.h