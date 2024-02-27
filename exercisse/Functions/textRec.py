# Create a program with the recording text function. It receives any text as a parameter and displays a diagrammed 
# message with lines above and below.


def head(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))


# message = str(input('Text space - ').title().strip())
head(str(input('Text space - ').title().strip()))
