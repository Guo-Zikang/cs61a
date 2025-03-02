(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond
  ((< num 0) -1)
  ((= num 0) 0)
  (else 1))
)


(define (square x) (* x x))

(define (pow x y)
  (if (= y 1)
      x
      (if (= (modulo y 2) 0)
        (square (pow x (/ y 2)))
        (* x (pow x (- y 1)))
      )
  )
)

