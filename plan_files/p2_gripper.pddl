(define (problem gripper-x-1)
   (:domain gripper-typed)
   (:objects boxA boxB - box
             B A - ball
			 lef right - gripper)
   (:init (at-robby boxA)
          (free left)
          (free right)
          (at B boxA)
          (at A boxA))
   (:goal (and (at B boxB)
               (at A boxB))))