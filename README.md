## RegExistentialCrisis

Experiments involving LLMs and their ability (or lack thereof) to understand regular expressions.

---

### Setup

TODO...

### Sample Output

```
QUESTION: "given the regex a*b?c+ does the string "abcc" matched by the regex?"
ANSWER[0]: Yes
Expected answer: yes
Correct!
-------------------
QUESTION: "given the regex a*b?c+ does the string "a" matched by the regex?"
ANSWER[0]: no
Expected answer: no
Correct!
-------------------
QUESTION: "given the regex a*b?c+ does the string "acc" matched by the regex?"
ANSWER[0]: Yes
Expected answer: yes
Correct!
-------------------
QUESTION: "given the regex a*b?c+ does the string "axc" matched by the regex?"
ANSWER[0]: No
Expected answer: no
Correct!
-------------------
QUESTION: "given the regex a*b?c+ does the string "ac" matched by the regex?"
ANSWER[0]: Yes
Expected answer: yes
Correct!
-------------------
QUESTION: "given the regex "a*b?c+" does the string "cx" matched by the regex?"
ANSWER[0]: no
Expected answer: no
Correct!
-------------------

Correct answers: 6
Incorrect answers: 0
Accuracy: 100.00%
```

