open Raylib

let sx = 10
let sy = 10

let w = 1000/sx
let he = 1000/sy

(*
*- - - > x (max w)
|
|
|
V
y (max h)


*)

type state = {
  tabl : float array array;
  time : int
}

let get t (x,y) = t.((he+y) mod he).((w+x) mod w)

let set t v (x,y) = 
  if x < 0 || x >= w || y < 0 || y >= he then failwith "nooog" 
  else t.(y).(x) <- v

let map = (List.map (fun i->i mod w,i/w) (List.init (w*he) Fun.id) )
let fold_left_map f zero = List.fold_left f zero map 
let iter_map f = List.iter f map

let copy_map a = 
  let a' = Array.make_matrix w he 0.0 in
  iter_map (fun pos -> set a' (get a pos) pos);
  a'

let (+$) (a,b) (a0,b0) = (a+a0,b+b0)  

let pond = [
   0.68; -0.9; 0.68;
   -0.9;-0.66; -0.9;
   0.68; -0.9; 0.68
 ]
(*let pond = [1.0;1.0;1.0;
1.0;9.0;1.0;
1.0;1.0;1.0]*)
let vois_pond = List.map2 (fun a b -> (a,b)) pond [
  (-1,-1);( 0,-1);(1,-1);
  (-1, 0);( 0, 0);(1, 0);
  (-1, 1);( 0, 1);(1, 1);
 ]

let activation x = if x < 0. then -.x else x
let activation x =  1.0 -. (2.0**(-0.6 *. x**2.0))
(*
let activation x =  if x = 3. || x = 11. || x = 12. then 1.0 else 0.0*)
(*-1./pow(2., (0.6*pow(x, 2.)))+1.;*)

let update state =  
  let t = copy_map state.tabl in
  let time = state.time in
  iter_map (fun pos -> 
      let value = 
        List.fold_left (+.) 0.0 (List.map (fun (v,pos)->v *. get state.tabl pos) (List.map (fun (v,p) -> v,pos+$p) vois_pond)) 
      in
      set t (activation value) pos);
  {tabl = t; time = (time + 1) mod 10}

let draw state =
  draw_rectangle 0 0 1000 1000 Color.black;
  iter_map (fun (x,y) ->
    let pos = (x,y) in
    draw_rectangle (x*sx) (y*sy) sx sy (color_from_hsv (get state.tabl pos *. 360.) 1. (get state.tabl pos));
    if false then draw_text (string_of_float (get state.tabl pos)) (sx*x) (sy*y) 10 Color.raywhite;
   );
  begin_drawing ();
  end_drawing ()

let rec loop state =
  if Raylib.window_should_close () then Raylib.close_window () else 
  if state.time mod 2 = 1 then draw state;
  let state' = update state in
  if is_mouse_button_down MouseButton.Left then
    set state'.tabl 1.0 (get_mouse_x ()/sx,get_mouse_y ()/sy);
  loop state'

let setup () =
  Random.self_init ();
  Raylib.init_window 1000 1000 "Jean";
  Raylib.set_target_fps 60;
  if is_window_ready () then
    let t = Array.make_matrix w he 0.0 in
    iter_map (fun pos -> set t (Random.float 2.0 -. 1.0)  pos);
    {tabl = t;time = 0}
   else failwith "window not ridi"
let () =
  let _ = loop (setup ()) in ()
