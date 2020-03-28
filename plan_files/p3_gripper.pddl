(define (problem gripper-x-1)
   (:domain gripper-typed)
   (:objects boxa boxb - box
             C B A - ball
			 lef right - gripper)
   (:init (at-robby boxa)
          (free left)
          (free right)
		  (at C boxa)
          (at B boxa)
          (at A boxa))
   (:goal (and (at B boxb)
			   (at C boxb)
               (at A boxb))))