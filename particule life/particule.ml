open Raylib

let w = 1000
let h = 1000
let sizex = 1000.0
let sizey = 1000.0
let rayon = 5.0
let friction = 0.1
let rs = 2.0
let nclan = 10

type vec = float * float

let gx = fst
let gy = snd
let zero = (0.0,0.0)
let (+$) (x1,y1) (x2,y2) = (x1+.x2,y1+.y2)
let ( *$) (x,y) c = (x*.c,y*.c)
let (-$) (x1,y1) (x2,y2) = (x1-.x2,y1-.y2)

let foi = float_of_int 
let iof = int_of_float
let abs_f x = if x < 0. then -.x else x 
let norme e = sqrt ((gx e)**2.0 +. (gy e)**2.0) 
(*pour les collisions*)
let dx = 0.1
let dy = 0.1

type point = {
  pos : vec;
  vit : vec;
  acc : vec;
  clan : int;
}

type demos = {
  min : float array array;
  max : float array array;
  k2 : float array array;
}
  
type status = {
  obj : point list;
  relations : demos;
  shift : vec;
}

let clans = Array.init nclan (fun i->fade (color_from_hsv (360. *. foi i /. foi nclan) 1. 1.) 0.5)   

let collision p = 
  let vx,vy = p.vit in
  if gx p.pos > sizex then 
    p.pos -$ p.vit -$ (dx,0.0), (-.vx,vy)
  else if gx p.pos < 0.0 then 
    p.pos -$ p.vit +$ (dx,0.0), (-.vx,vy)
  else if gy p.pos > sizey then 
    p.pos -$ p.vit -$ (0.0,dy), (vx,-.vy)
  else if gy p.pos < 0.0 then 
    p.pos -$ p.vit +$ (0.0,dy), (vx,-.vy)
  else
    p.pos +$ p.vit, p.vit 

(*force de répulsion*)
let f r k2 minR maxR = 
    if r < minR then rs *. minR *. ( 1.0 /. (minR +. rs) -. 1.0 /. (r+.rs))
    else if r < maxR then k2 *. (1.0 -. abs_f (2.0 *. r -. (minR+.maxR)) /. (maxR -. minR))
    else 0.0

let attraction relations a b =
  if a = b then zero else
  let e = b.pos -$ a.pos in
  let d = norme e in
  let er = e *$ (1.0/.d) in
  let k2 = relations.k2.(a.clan).(b.clan) in 
  let minR = relations.min.(a.clan).(b.clan) in
  let maxR = relations.max.(a.clan).(b.clan) in
  er *$ (f d k2 minR maxR)

let move status p =
  let others = status.obj in
  let relations = status.relations in
  let pos, vit = collision p in
  {
    pos = pos;
    vit = vit *$ (1.0 -. friction) +$ p.acc;
    acc = List.fold_left (+$) zero  (List.map (attraction relations p)  others);
    clan = p.clan
  }
  
let draw status =
  begin_drawing ();
  draw_rectangle 0 0 w h (fade Color.black 0.1);
  List.iter (fun p -> 
    let pos = p.pos +$ status.shift in
    draw_circle (iof (fst pos)) (iof (snd pos)) 10. clans.(p.clan)) status.obj;
  end_drawing ()

let update s =
  let obj' = List.map (move s) s.obj in
  let vit = 10.0 in
  {
    obj = obj'; 
    relations = s.relations; 
    shift = s.shift 
        +$ if is_key_down Key.H then (1.,0.) *$vit else zero
        +$ if is_key_down Key.J then (0.,-1.) *$vit else zero 
        +$ if is_key_down Key.K then (0.,1.) *$vit else zero
        +$ if is_key_down Key.L then (-1.,0.) *$vit else zero
}

let rec loop status =
  if window_should_close () then close_window () else
    draw status;
    loop (update status) 

let rand_vec deb fin =
  (
    Random.float (fin -. deb) +. deb,
    Random.float (fin -. deb) +. deb
  )

let setup () =
  Random.self_init ();
  init_window w h "Jeanne d'Arc";
  set_target_fps 60;
  let obj = 
    List.init 200 (fun _ -> {
      pos = rand_vec 0.0 1000.0;
      vit = rand_vec (-10.0) 10.0;
      acc = rand_vec (-10.0) 10.0; 
      clan = Random.int nclan}
   ) in
  let tk2 = Array.make_matrix nclan nclan 1.0 in
  let minR = Array.make_matrix nclan nclan 0.0 in
  let maxR = Array.make_matrix nclan nclan 0.0 in
  for i = 0 to nclan-1 do
    for j = 0 to nclan-1 do
      tk2.(i).(j) <- (let v = cos (Random.float 6.14 -. 3.14) /.2.0 -. 0.2 in if i=j then -. abs_f v else v);
      minR.(i).(j) <- max rayon (Random.float 30.0);
      maxR.(i).(j) <- Random.float 70.0 +. 30.0;
      maxR.(j).(i) <- maxR.(i).(j); (*radii ?*)
    done
  done;
  {
    obj = obj; 
    relations = {
      k2 = tk2;
      min = minR;
      max = maxR;
    };
    shift = zero
  }

let () =
  let _ = loop (setup ()) in ()


