text = """
paren-match $ cat stretch.rkt
#lang racket

(struct Q (x y) #:transparent)

;; returns true if given q1 and q2 do not conflict
(define (safe? q1 q2)
  (match* (q1 q2)
    [((Q x1 y1) (Q x2 y2))
     (not (or (= x1 x2) (= y1 y2)
              (= (abs (- x1 x2)) (abs (- y1 y2)))))]))

;; returns true if given q doesn't conflict with anything in given list of qs
(define (safe-lst? q qs) (for/and ([q2 qs]) (safe? q q2)))

(define (nqueens n)
  ;; qs is partial solution; x y is current position to try
  (let loop ([qs null] [x 0] [y 0])
    (cond [(= (length qs) n) qs] ; found a solution
          [(>= x n) (loop qs 0 (add1 y))] ; go to next row
          [(>= y n) #f] ; current solution is invalid
          [else
           (define q (Q x y))
           (if (safe-lst? q qs) ; is current position safe?
               (or (loop (cons q qs) 0 (add1 y)) ; optimistically place a queen
                                                ; (and move pos to next row)
                   (loop qs (add1 x) y)) ; backtrack if it fails
               (loop qs (add1 x) y)))))

(nqueens 8)
; => (list (Q 3 7) (Q 1 6) (Q 6 5) (Q 2 4) (Q 5 3) (Q 7 2) (Q 4 1) (Q 0 0))
paren-match $
"""


# write function to give position of not closed (, [, { in text
def detect_not_closed(text):
    """
    O(n) time complexity

    O(n) space complexity

    :param text: string

    :return: position of not closed (, [, { in text
    """
    open_stack = []
    open_chars = "([{"
    close_chars = ")]}"
    expect_chars = dict(zip(open_chars, close_chars))

    for pos, c in enumerate(text):
        if c in open_chars:
            open_stack.append((pos, c))
        elif c in close_chars:
            if not open_stack:
                return pos
            last_open_pos, last_open = open_stack.pop()
            expect_close = expect_chars[last_open]
            if c != expect_close:
                return last_open_pos

        else:
            continue
    if open_stack:
        last_open_pos, last_open = open_stack.pop()
        return last_open_pos
    return -1


# write function to give position of not closed (, [, { in text


test_cases = [
    ("([])[()]", -1),
    ("([])[(]", 5),
    ("([)]", 1),
    (text, 714),
    ("[", 0),
    ("{", 0),
    ("[)", 0),
    ("{)", 0),
    ("[}", 0),
    ("{]", 0),
    ("[()]{", 4),
    ("[]{()", 2),
    ("[()]}()", 4),
    ("}", 0),
    ("}}[]", 0),
    ("([{()}]", 0),
    ("", -1),
]


for text, expected in test_cases:
    result = detect_not_closed(text)
    _range = 3
    assert (
        result == expected
    ), f"text: <{text}>, Expected {expected}, but got {result}, here is the slice: <{text[result-_range:result+_range]}>"
