import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../api/axios";

import {
  User,
  Mail,
  Award,
  Brain,
  CheckCircle,
  Target,
  Rocket,
  BookOpen,
  Sparkles,
  TrendingUp,
  GraduationCap
} from "lucide-react";

import {
  ResponsiveContainer,
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";


function StudentProfile(){

const {id}=useParams();

const [student,setStudent]=useState(null);


useEffect(()=>{

loadStudent();

},[]);



const loadStudent=async()=>{

try{

const res=await api.get(
`/dashboard/student/${id || 1}`
);


setStudent(res.data);


}

catch(error){

console.log(
error.response?.data || error.message
);

}

};





if(!student){

return(

<div className="
min-h-screen
flex
items-center
justify-center
">


<div className="text-center">


<Sparkles
size={60}
className="
mx-auto
text-blue-600
animate-pulse
"
/>


<h2 className="
text-3xl
font-bold
mt-5
">

Loading AI Student Profile...

</h2>


</div>


</div>

)

}





return(

<div className="
min-h-screen
bg-slate-100
">



{/* HEADER */}


<div className="
bg-gradient-to-r
from-blue-700
to-indigo-800
text-white
shadow-xl
">


<div className="
max-w-7xl
mx-auto
px-8
py-8
flex
justify-between
items-center
">


<div>


<h1 className="
text-4xl
font-bold
">

AI Student Profile

</h1>


<p className="
text-blue-100
mt-2
">

AI Powered Student Analytics

</p>


</div>



<div className="
bg-white
text-blue-700
rounded-full
p-3
">

<GraduationCap size={35}/>

</div>


</div>


</div>





<div className="
max-w-7xl
mx-auto
p-8
">



{/* PROFILE CARD */}


<div className="
bg-white
rounded-2xl
shadow-xl
p-8
">


<div className="
flex
items-center
gap-6
">


<div className="
w-24
h-24
rounded-full
bg-gradient-to-r
from-blue-500
to-indigo-700
flex
items-center
justify-center
text-white
">


<User size={50}/>


</div>



<div>


<h2 className="
text-3xl
font-bold
">

{student.name}

</h2>



<p className="
flex
items-center
gap-2
text-gray-600
mt-3
">

<Mail size={18}/>

{student.email || "Not Available"}

</p>


</div>



</div>


</div>





{/* STAT CARDS */}


<div className="
grid
md:grid-cols-2
xl:grid-cols-4
gap-6
mt-8
">


<Stat

title="Engineering Score"

value={`${student.engineering_score || 0}%`}

icon={<Award/>}

/>


<Stat

title="Level"

value={student.level}

icon={<Brain/>}

/>


<Stat

title="Job Ready"

value={student.job_readiness}

icon={<CheckCircle/>}

/>


<Stat

title="Skills"

value={student.skill_count}

icon={<TrendingUp/>}

/>


</div>
{/* TECHNICAL SKILLS */}


<div className="
bg-white
rounded-2xl
shadow-xl
p-8
mt-10
">


<h2 className="
text-2xl
font-bold
flex
items-center
gap-3
mb-6
">


<Brain className="text-blue-600"/>

Technical Skills


</h2>




<div className="
grid
md:grid-cols-2
xl:grid-cols-3
gap-6
">


{
(student.skills || []).map((skill,index)=>(


<div

key={index}

className="
border
rounded-xl
p-5
hover:shadow-lg
transition
"

>


<div className="
flex
justify-between
">

<h3 className="
font-bold
text-lg
">

{skill.name}

</h3>



<span className="
font-bold
text-blue-600
">

{skill.score}%

</span>


</div>




<div className="
w-full
bg-gray-200
h-3
rounded-full
mt-4
">


<div

className="
h-3
rounded-full
bg-gradient-to-r
from-blue-500
to-purple-600
"

style={{

width:`${skill.score}%`

}}

/>


</div>



<p className="
text-gray-500
mt-4
">

Technical proficiency based on AI analysis.

</p>



</div>


))


}



</div>


</div>







{/* AI INTELLIGENCE */}



<div className="
grid
md:grid-cols-3
gap-6
mt-10
">





{/* CAREER */}



<div className="
bg-white
rounded-2xl
shadow-xl
p-8
">


<div className="
flex
items-center
gap-3
">


<Target
className="text-purple-600"
/>


<h2 className="
text-xl
font-bold
">

Career Prediction

</h2>


</div>




<p className="
text-gray-500
mt-6
">

Recommended Role

</p>




<h3 className="
text-3xl
font-bold
text-purple-700
mt-2
">

{
student.career_prediction?.role ||
"Not Generated"
}

</h3>





<div className="mt-6">


<div className="
flex
justify-between
">


<span>

Confidence

</span>


<span className="
font-bold
text-green-600
">

{
student.career_prediction?.confidence || 0
}%

</span>


</div>




<div className="
w-full
bg-gray-200
h-3
rounded-full
mt-3
">


<div

className="
h-3
rounded-full
bg-gradient-to-r
from-purple-500
to-blue-600
"


style={{

width:`${
student.career_prediction?.confidence || 0
}%`

}}

/>


</div>


</div>





<div className="
mt-8
bg-green-100
text-green-700
rounded-xl
p-3
text-center
font-bold
">

Internship Ready

</div>



</div>








{/* LEARNING FOCUS */}



<div className="
bg-white
rounded-2xl
shadow-xl
p-8
">


<div className="
flex
items-center
gap-3
">


<Rocket
className="text-blue-600"
/>


<h2 className="
text-xl
font-bold
">

Learning Focus

</h2>


</div>





<div className="
space-y-4
mt-6
">


{

(student.learning_focus || []).map(

(item,index)=>(


<div

key={index}

className="
font-semibold
"

>

✅ {item}

</div>


)

)


}



</div>


</div>








{/* AI RECOMMENDATION */}



<div className="
bg-white
rounded-2xl
shadow-xl
p-8
">


<div className="
flex
items-center
gap-3
">


<Sparkles
className="text-yellow-500"
/>


<h2 className="
text-xl
font-bold
">

AI Recommendation

</h2>


</div>




<p className="
text-gray-600
mt-6
leading-7
">


Student profile matches modern AI internship
requirements based on skills, projects and
engineering progress.


</p>




<div className="
mt-8
bg-gradient-to-r
from-green-500
to-emerald-600
text-white
rounded-xl
p-4
text-center
font-bold
">

🚀 Ready For AI Internship

</div>



</div>




</div>







{/* PROGRESS + MISSING SKILLS */}


<div className="
grid
md:grid-cols-2
gap-8
mt-10
">



<div className="
bg-white
rounded-2xl
shadow-xl
p-8
">


<h2 className="
text-2xl
font-bold
flex
gap-3
items-center
">


<TrendingUp
className="text-blue-600"
/>


AI Engineering Progress


</h2>




<div className="
flex
justify-center
mt-10
">


<div className="
w-44
h-44
rounded-full
bg-gradient-to-r
from-blue-600
to-purple-600
flex
items-center
justify-center
">


<div className="
w-32
h-32
bg-white
rounded-full
flex
items-center
justify-center
">


<span className="
text-4xl
font-bold
text-blue-700
">


{student.engineering_score || 0}%


</span>


</div>


</div>


</div>




<p className="
text-center
text-gray-500
mt-8
">

Overall AI readiness based on skills,
projects and roadmap.

</p>



</div>





<div className="
bg-white
rounded-2xl
shadow-xl
p-8
">


<h2 className="
text-2xl
font-bold
flex
gap-3
items-center
">


<Target className="text-red-500"/>


Missing Skills


</h2>




<div className="
space-y-4
mt-6
">


{

(student.missing_skills || []).map(

(skill,index)=>(


<div

key={index}

className="
bg-red-50
border
rounded-xl
p-4
"

>

⚠ {skill}

</div>


)


)


}


</div>


</div>



</div>
{/* AI ROADMAP TIMELINE */}


<div className="
bg-white
rounded-2xl
shadow-xl
p-8
mt-10
">


<h2 className="
text-2xl
font-bold
flex
items-center
gap-3
">


<BookOpen className="text-blue-600"/>

AI Internship Roadmap Timeline


</h2>




<div className="
grid
md:grid-cols-4
gap-6
mt-8
">


{

(student.roadmap || []).map(

(item,index)=>(


<RoadmapCard

key={index}

week={item.week}

title={item.title}

/>


)


)


}


</div>


</div>








{/* ENGINEERING PERFORMANCE */}



<div className="
bg-white
rounded-2xl
shadow-xl
p-8
mt-10
">


<h2 className="
text-2xl
font-bold
flex
items-center
gap-3
">


<TrendingUp className="text-green-600"/>

Engineering Performance


</h2>




<div className="
mt-8
h-80
">


<ResponsiveContainer

width="100%"

height="100%"

>


<LineChart

data={[

{
name:"Week 1",
score:60
},

{
name:"Week 2",
score:70
},

{
name:"Week 3",
score:80
},

{
name:"Week 4",
score:student.engineering_score || 80
}


]}

>


<CartesianGrid strokeDasharray="3 3"/>


<XAxis dataKey="name"/>


<YAxis/>


<Tooltip/>



<Line

type="monotone"

dataKey="score"

stroke="#2563eb"

strokeWidth={4}

/>


</LineChart>


</ResponsiveContainer>



</div>


</div>









{/* CASE STUDIES */}



<div className="
bg-white
rounded-2xl
shadow-xl
p-8
mt-10
">


<h2 className="
text-2xl
font-bold
flex
items-center
gap-3
">


<BookOpen/>


Recent Case Studies


</h2>





<div className="
space-y-4
mt-6
">


{


student.case_studies?.length ?


student.case_studies.map(

(item,index)=>(


<div

key={index}

className="
border
rounded-xl
p-5
hover:shadow-lg
transition
"


>


<h3 className="
font-bold
text-lg
">


✅ {item.title}


</h3>




<p className="mt-2 text-gray-600">

Technology:
{" "}
{item.technology}

</p>




<p>

Difficulty:
{" "}
{item.difficulty}

</p>



<p>

Status:
{" "}
{item.status}

</p>




<p>

Score:
{" "}
{item.score}%

</p>



</div>


)


)



:


<p className="
text-gray-500
">

No Case Studies Available

</p>


}



</div>


</div>









{/* AI INSIGHTS */}



<div className="
bg-gradient-to-r
from-indigo-600
to-purple-700
text-white
rounded-2xl
shadow-xl
p-8
mt-10
">


<h2 className="
text-2xl
font-bold
">

🧠 AI Insights

</h2>




<p className="
mt-6
leading-8
">


Student demonstrates strong AI engineering
potential. Improving LLM, MLOps, Docker and
cloud deployment skills will increase career
opportunities.


</p>


</div>



</div>


</div>


);

}







function Stat({title,value,icon}){


return(


<div className="
bg-white
rounded-2xl
shadow-xl
p-6
hover:scale-105
transition
">


<div className="
flex
justify-between
items-center
">


<div>


<p className="text-gray-500">

{title}

</p>



<h2 className="
text-3xl
font-bold
mt-2
">

{value}

</h2>


</div>




<div className="
w-14
h-14
rounded-xl
bg-gradient-to-r
from-blue-600
to-indigo-700
text-white
flex
items-center
justify-center
">


{icon}


</div>


</div>


</div>


)

}








function RoadmapCard({week,title}){


return(


<div className="
border
rounded-2xl
p-6
hover:shadow-xl
transition
">


<h3 className="
text-blue-600
font-bold
text-lg
">

{week}

</h3>




<p className="
mt-3
font-semibold
">

{title}

</p>




<div className="
mt-5
bg-green-100
text-green-700
px-4
py-2
rounded-full
inline-block
font-semibold
">

✓ Planned

</div>


</div>


)


}





export default StudentProfile;