This is a code-guessing game written in Python.
I have seen it called many names, like Cows and
Bulls, but I call it Mastermind.

The computer thinks of a 4-digit code, like:
        --->>    5912    <<---
and you have to guess it. With each guess, you
are scored like this:

X = Right digit, right place, like 5732 XX
    The 5 and 2 correctly match the code.

o = Right digit, in wrong place, like 7825 oo
    5 and 2 are in the code, but in wrong places

Often there is a result like 5726 - Xo - one
digit is in the right place, one is in the wrong
place, and two aren't in the code at all. The order
of Xs and os is random, so you don't know which
digit they are for.

Roland Waddilove
