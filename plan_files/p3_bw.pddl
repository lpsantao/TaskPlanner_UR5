(define (problem BLOCKS-4-2)
(:domain BLOCKS)
(:objects B C A - block)
(:INIT (CLEAR A) (CLEAR C) (ONTABLE A) (ONTABLE B) (ON C B) (HANDEMPTY))
(:goal (AND (ON A B) (ON B C)))
)