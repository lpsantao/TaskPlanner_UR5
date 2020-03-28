(define (problem gripper-x-2)
   (:domain gripper-typed)
   (:objects boxa boxb - box
             D C B A - ball
			 left right - gripper)
   (:init (at-robby boxa)
          (free left)
          (free right)
          (at D boxa)
          (at C boxa)
          (at B boxa)
          (at A boxa))
   (:goal (and (at D boxb)
               (at C boxb)
               (at B boxb)
               (at A boxb))))