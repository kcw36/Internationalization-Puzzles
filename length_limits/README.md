# Puzzle 1 - Length Limits

The venerable SMS system uses a message limit of 160 bytes1. This was designed so that a message could fit in exactly one packet, thus being really cheap and fast to handle on first-generation mobile phone networks. Although the approach makes sense for technical reasons, it unfairly penalizes people who use non-latin (e.g. Russian, Greek, Japanese) alphabets - in most encodings, they need more bytes per character than latin alphabets.

Twitter used to have a character limit of 140 characters2. But this is a limit by design, to emphasize the concise and ephemeral nature of the platform. It's not a technical limitation. So the designers of twitter set the limit at 140 characters, NOT the number of bytes.

You are working for a fictious company named "TOPlap", which sends messages to customers using both SMS and Twitter, via a message broker. The message broker charges a fee for each message sent, as follows:

For each SMS: 11 cents.
For each Tweet: 7 cents.
Discount rate for messages sent as SMS and Tweet together: 13 cents.
Write a program that checks whether messages are valid as SMS and / or valid as (old-style) Tweet3. Your input is a list of messages in different languages, one on each line, in UTF-8 format. The message broker expects UTF-8 format as well. Calculate your total bill with the message broker, assuming that you will not send any messages that are too long. So a message that is valid for the SMS platform, but not as tweet, will only incur the charge of 11 cents for a single SMS message.

Line endings are excluded from byte count as well as character count.

What is the total cost of all your messages, in cents?