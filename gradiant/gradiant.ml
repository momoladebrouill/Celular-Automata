
open Raylib
type carre = (int*int)
let w = 100
let he = 100

(*
*- - - > x (max w)
|
|
|
V
y (max h)


*)

module Ens = Set.Make(struct 
  type t = carre 
  let compare (x1,y1) (x2,y2) =  
    Stdlib.compare (x1 + y1 * w) (x2 + y2*w) 
end)

type state = {
  mutable carr : Ens.t;
  value : (carre,float) Hashtbl.t;
  time : float
}

let fold_left_map f zero =
  List.fold_left f zero (List.map (fun i->i mod w,i/w) (List.init (w*he) Fun.id) )

let (+$) (a,b) (a0,b0) = (a+a0,b+b0)  

let get s h (x,y) = 
  if x < 0 || x >= w || y < 0 || y >= he then 0.0 
  else if Ens.mem (x,y) s then Hashtbl.find h (x,y)
  else 0.0


let vois = [(-1,-1);(-1,0);(-1,1);(0,-1);(0,1);(1,-1);(1,0);(1,1)]
let vois_pond = List.map (fun pos -> ((Random.float 2.0),pos)) ((0,0)::vois)

let set s h v pos =
  Hashtbl.replace h pos v;
  Ens.add pos s 

let activation = Fun.id

let update state =  

  let s = state.carr in
  let h = state.value in
  let time = state.time in
  let s' = 
    fold_left_map (fun s' pos -> 
      let value = (List.fold_left (+.) 0.0 (List.map (fun (v,pos)->v *. get s h pos) (List.map (fun (v,p) -> v,pos+$p) vois_pond)))/.8. in
      if value > 0.125  then set s' h value pos  
      (*else if Random.int 50000 = 0 then List.fold_left (fun s' dir -> set s' h 1.0 (pos +$ dir)) s' ((0,0)::vois)*)
      else s') Ens.empty
  in 
  {carr = s'; value = h; time = if time = 100.0 then 0.0  else time +. 1.0}

let rec loop state =
  if Raylib.window_should_close () then Raylib.close_window () else 
  let domain = Domain.spawn (fun _ -> update state) in 
  draw_rectangle 0 0 1000 1000 Color.black;
  Ens.iter (fun (x,y) ->
    draw_rectangle (x*10) (y*10) 10 10 (color_from_hsv 360. 1. (Hashtbl.find state.value (x,y)) ))
    state.carr;
  begin_drawing ();
  end_drawing ();
  if is_mouse_button_down MouseButton.Left then
    state.carr <- set state.carr state.value 1.0 (get_mouse_x ()/10,get_mouse_y ()/10);
  loop (Domain.join domain)

let setup () =
  Random.self_init ();
  Raylib.init_window 1000 1000 "Jean";
  Raylib.set_target_fps 60;
  if is_window_ready () then
    let h = Hashtbl.create 69 in
    let s = fold_left_map (fun s pos -> if Random.int 10 <> 0 then s else (Hashtbl.add h pos 1.0;Ens.add pos s) ) Ens.empty in 
    {carr = s; value = h; time = 0.0}
   else failwith "window not ridi"
let () =
  let _ = loop (setup ()) in ()
