(define (domain gripper-typed)
   (:requirements :strips)
   (:types box ball gripper)
   (:predicates (at-robby ?r - box)
		(at ?b - ball ?r - box)
		(free ?g - gripper)
		(carry ?o - ball ?g - gripper))

   (:action move
       :parameters  (?from ?to - box)
       :precondition (at-robby ?from)
       :effect (and  (at-robby ?to)
		     (not (at-robby ?from))))



   (:action pick
       :parameters (?obj - ball ?box - box ?gripper - gripper)
       :precondition  (and  (at ?obj ?box) (at-robby ?box) (free ?gripper))
       :effect (and (carry ?obj ?gripper)
		    (not (at ?obj ?box))
		    (not (free ?gripper))))


   (:action drop
       :parameters  (?obj - ball ?box - box ?gripper - gripper)
       :precondition  (and  (carry ?obj ?gripper) (at-robby ?box))
       :effect (and (at ?obj ?box)
		    (free ?gripper)
		    (not (carry ?obj ?gripper)))))



