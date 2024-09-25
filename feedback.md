# Feedback
As per usual, your git practices are wonderful - commit messages are clear and concise and you have taken the time to ensure that everything is 'production-ready'!

Queue:
- I'm not sure that I would have the default of the queue's max_size be `None`, it seems somewhat counterintuitive to what a max_size should be. That being said, it depends on the intention of the queue, so if the intention is that the user should always define a max_size, then I would suggest that a default of 'None' is irrelevant - as it should refuse to be created if nothing is given. _However_, if the intention is that unless specified, there should not be a max_size, then I would make that explicit that it can never be full.
- An interesting addition to your queue might be something along the lines of 'find_key_of', a method in which a user can enter the value as a string and the return value is the key of said value.

This is lovely testing and implementation throughout. I would like to see you practise building your own logic via the 'find_key_of' or another method that you implement from scratch for your queue (including a test suite!)
