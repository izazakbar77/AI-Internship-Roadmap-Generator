import React, {useEffect, useState} from "react";
import api from "../api/axios";

import {
    BookOpen,
    Plus,
    Trash2,
    Code2,
    Award,
    Clock,
    CheckCircle
} from "lucide-react";



function CaseStudies(){


const [cases,setCases]=useState([]);


const [form,setForm]=useState({

    student_id:1,
    title:"",
    technology:"",
    difficulty:"Easy",
    status:"Pending",
    score:0

});





useEffect(()=>{

    loadCases();

},[]);






const loadCases=async()=>{

try{

const res = await api.get(
    "/case-studies/"
);


setCases(res.data);


}
catch(error){

console.log(error);

}


};







const addCase=async()=>{


try{


await api.post(

"/case-studies/",

form

);



setForm({

student_id:1,
title:"",
technology:"",
difficulty:"Easy",
status:"Pending",
score:0

});



loadCases();



}
catch(error){

console.log(
error.response?.data || error
);

}


};








const deleteCase=async(id)=>{


try{


await api.delete(

`/case-studies/${id}`

);



loadCases();



}
catch(error){

console.log(error);

}


};








return(


<div className="
min-h-screen
bg-gray-100
p-8
">



<h1 className="
text-3xl
font-bold
mb-8
">

AI Case Studies

</h1>







<div className="
grid
md:grid-cols-2
gap-8
">






{/* FORM */}


<div className="
bg-white
rounded-xl
shadow
p-6
">



<h2 className="
text-xl
font-bold
mb-5
flex
gap-2
">

<Plus/>

Add Case Study

</h2>






<input

placeholder="Case Study Title"

value={form.title}

onChange={(e)=>

setForm({

...form,

title:e.target.value

})

}

className="
w-full
border
p-3
rounded-lg
mb-4
"

/>






<input

placeholder="Technology"

value={form.technology}

onChange={(e)=>

setForm({

...form,

technology:e.target.value

})

}

className="
w-full
border
p-3
rounded-lg
mb-4
"

/>







<select

value={form.difficulty}

onChange={(e)=>

setForm({

...form,

difficulty:e.target.value

})

}

className="
w-full
border
p-3
rounded-lg
mb-4
"

>


<option>Easy</option>
<option>Medium</option>
<option>Hard</option>


</select>






<select

value={form.status}

onChange={(e)=>

setForm({

...form,

status:e.target.value

})

}

className="
w-full
border
p-3
rounded-lg
mb-4
"

>


<option>Pending</option>
<option>Completed</option>
<option>Review</option>


</select>







<input

type="number"

placeholder="Score"

value={form.score}

onChange={(e)=>

setForm({

...form,

score:Number(e.target.value)

})

}

className="
w-full
border
p-3
rounded-lg
mb-5
"

/>







<button

onClick={addCase}

className="
w-full
bg-blue-600
text-white
py-3
rounded-xl
font-bold
"

>


Save Case Study


</button>






</div>










{/* LIST */}



<div className="
bg-white
rounded-xl
shadow
p-6
">


<h2 className="
text-xl
font-bold
mb-5
">

All Case Studies

</h2>





{

cases.map((item)=>(



<div

key={item.id}

className="
border
rounded-xl
p-5
mb-5
"

>



<div className="
flex
justify-between
">


<div className="
bg-blue-100
p-3
rounded-full
text-blue-600
">


<BookOpen/>


</div>



<button

onClick={()=>deleteCase(item.id)}

className="
text-red-600
"

>

<Trash2/>

</button>



</div>







<h2 className="
text-xl
font-bold
mt-4
">

{item.title}

</h2>





<p className="
mt-3
flex
gap-2
items-center
">

<Code2 size={18}/>

{item.technology}

</p>







<p className="
mt-3
flex
gap-2
items-center
">

<Award size={18}/>

Difficulty:

{item.difficulty}

</p>







<p className="
mt-3
flex
gap-2
items-center
">

<Clock size={18}/>

Status:

{item.status}

</p>







<p className="
mt-3
flex
gap-2
items-center
">

<CheckCircle size={18}/>

Score:

{item.score}%

</p>






</div>



))

}




</div>






</div>






</div>


)


}



export default CaseStudies;