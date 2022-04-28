# The (Work) Lingo Bingo

Finally, you will pay attention to your meetings.

## What it is? 

1. A Bingo game based on the most often used (key)words during your work meetings. Ex: (high) availability, scalability and maintainability.
2. An opportunity for any developer to make contributions so we can share knowledges and apply best practices from Agile Management to less important things (such as coding).
3. An attempt to make the following statement return true: Having development hours is something that pay off.
4. An opportunity for learning: Software Engineering, programming (Python, at first, but not limited to it), CD/CI ? Containerization (some Kubernets + Docker)? Queues (Kafka, Rabbit MQ, other?) 
5.Solo, at first, and, in the near future, multiplayer.

## What it is not?

1. A joke, a meaningless provocation in itself
2. An exceuse not to work
3. Boring

## How does it work?

1. You will execute the python script just like the following:

	```python3 lingobingo.py```

2. You will be prompeted to load the default list of inputs or to inform another source (of bingo words), that can be any file, in any format, since you inform the word separation character ("," , ";", ":", "-", etc).
3. You will select the size of your bingo board: 3x3, 4x4, 4x6, etc.
4. The game will start after reading the input of step 3: Each time you hear a word available in your board, you mark (or type the word, depending on the version you are using) that one word in order to keep it highlighted.
5.The round finishes every time you highlight the words of an entire line or an entire column (eventually both - it's possible)
