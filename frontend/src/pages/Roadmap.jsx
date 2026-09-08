import React, { useState } from "react";
import api from "../api/axios";

import {
    Sparkles,
    Target,
    Calendar,
    BookOpen,
    CheckCircle,
    Map,
    Cpu,
    Rocket,
    TrendingUp
} from "lucide-react";

function Roadmap() {

    const [loading, setLoading] = useState(false);
    const [roadmap, setRoadmap] = useState(null);

    const [form, setForm] = useState({
        engineering_level: "Intermediate",
        missing_skills: "",
        target_role: "AI Engineer",
        internship_duration: 3
    });

    const generateRoadmap = async () => {

        try {

            setLoading(true);

            const response = await api.post("/roadmap/", {

                engineering_level: form.engineering_level,

                missing_skills: form.missing_skills
                    .split(",")
                    .map(skill => skill.trim())
                    .filter(skill => skill !== ""),

                target_role: form.target_role,

                internship_duration: Number(form.internship_duration)

            });

            setRoadmap(response.data);

        } catch (error) {

            console.log(error.response?.data || error);

        } finally {

            setLoading(false);

        }

    };

    return (

<div className="min-h-screen bg-slate-100 p-8">

<div className="max-w-7xl mx-auto">

<div className="bg-gradient-to-r from-blue-700 via-indigo-700 to-purple-700 rounded-3xl shadow-xl p-8 mb-8 text-white">

<div className="flex items-center gap-4">

<div className="bg-white/20 p-4 rounded-2xl">

<Rocket size={40}/>

</div>

<div>

<h1 className="text-4xl font-bold">
AI Internship Roadmap
</h1>

<p className="opacity-90 mt-2">
Generate Personalized AI Career Roadmap
</p>

</div>

</div>

</div>

<div className="grid lg:grid-cols-3 gap-8">

{/* LEFT PANEL */}

<div className="lg:col-span-1">

<div className="bg-white rounded-2xl shadow-lg p-6">

<h2 className="text-xl font-bold mb-6 flex items-center gap-2">

<Sparkles className="text-purple-600"/>

Generate Roadmap

</h2>

<input
className="w-full border rounded-xl p-3 mb-4"
placeholder="Engineering Level"
value={form.engineering_level}
onChange={(e)=>
setForm({
...form,
engineering_level:e.target.value
})}
/>

<input
className="w-full border rounded-xl p-3 mb-4"
placeholder="Target Role"
value={form.target_role}
onChange={(e)=>
setForm({
...form,
target_role:e.target.value
})}
/>

<input
className="w-full border rounded-xl p-3 mb-4"
placeholder="Missing Skills (Comma Separated)"
value={form.missing_skills}
onChange={(e)=>
setForm({
...form,
missing_skills:e.target.value
})}
/>

<input
type="number"
className="w-full border rounded-xl p-3 mb-5"
placeholder="Internship Duration (Months)"
value={form.internship_duration}
onChange={(e)=>
setForm({
...form,
internship_duration:e.target.value
})}
/>

<button
onClick={generateRoadmap}
className="w-full bg-blue-600 hover:bg-blue-700 text-white rounded-xl py-3 font-bold transition"
>

{loading ? "Generating..." : "Generate AI Roadmap"}

</button>

</div>

</div>

{/* RIGHT PANEL */}

<div className="lg:col-span-2">

{roadmap && (

<div className="space-y-6">
    {/* Top Information */}

<div className="bg-white rounded-2xl shadow-lg p-6">

<div className="flex justify-between items-center">

<div>

<h2 className="text-3xl font-bold">

{roadmap.target_role}

</h2>

<p className="text-gray-500 mt-2">

Engineering Level :

<span className="ml-2 font-semibold text-blue-600">

{roadmap.engineering_level}

</span>

</p>

<p className="text-gray-500 mt-2">

Estimated Graduation :

<span className="ml-2 font-semibold text-green-600">

{roadmap.estimated_graduation}

</span>

</p>

</div>

<Target
size={60}
className="text-blue-600"
/>

</div>

<div className="mt-8">

<div className="flex justify-between mb-2">

<span className="font-semibold">

Internship Progress

</span>

<span className="font-bold text-blue-600">

75%

</span>

</div>

<div className="w-full h-4 bg-gray-200 rounded-full">

<div
className="h-4 rounded-full bg-gradient-to-r from-blue-500 via-indigo-500 to-purple-600"
style={{ width: "75%" }}
/>

</div>

</div>

</div>



{/* Weekly Goals */}

<div className="bg-white rounded-2xl shadow-lg p-6">

<h2 className="text-2xl font-bold flex items-center gap-2 mb-5">

<Calendar className="text-green-600"/>

Weekly Goals

</h2>

<div className="grid md:grid-cols-2 gap-4">

{roadmap.weekly_goals.map((goal,index)=>(

<div
key={index}
className="border rounded-xl p-4 hover:shadow-lg transition"
>

<div className="flex gap-3">

<CheckCircle className="text-green-600"/>

<p>{goal}</p>

</div>

</div>

))}

</div>

</div>



{/* Monthly Goals */}

<div className="bg-white rounded-2xl shadow-lg p-6">

<h2 className="text-2xl font-bold flex items-center gap-2 mb-5">

<BookOpen className="text-orange-600"/>

Monthly Goals

</h2>

<div className="grid md:grid-cols-2 gap-4">

{roadmap.monthly_goals.map((goal,index)=>(

<div
key={index}
className="bg-orange-50 border border-orange-200 rounded-xl p-4"
>

<div className="flex gap-3">

<Calendar className="text-orange-600"/>

<p>{goal}</p>

</div>

</div>

))}

</div>

</div>
{/* Recommended Projects */}

<div className="bg-white rounded-2xl shadow-lg p-6">

<h2 className="text-2xl font-bold flex items-center gap-2 mb-5">

<Rocket className="text-purple-600"/>

Recommended Projects

</h2>

<div className="grid md:grid-cols-3 gap-4">

{roadmap.recommended_projects.map((project,index)=>(

<div
key={index}
className="rounded-xl p-5 bg-gradient-to-r from-purple-500 to-indigo-600 text-white shadow-lg"
>

<Rocket
size={30}
className="mb-3"
/>

<h3 className="font-bold text-lg">

{project}

</h3>

</div>

))}

</div>

</div>



{/* Recommended Case Study */}

<div className="bg-white rounded-2xl shadow-lg p-6">

<h2 className="text-2xl font-bold flex items-center gap-2 mb-5">

<BookOpen className="text-indigo-600"/>

Recommended Case Study

</h2>

<div className="rounded-xl bg-gradient-to-r from-indigo-500 to-purple-600 text-white p-6">

<BookOpen
size={35}
className="mb-4"
/>

<h3 className="text-2xl font-bold">

{roadmap.recommended_case_study}

</h3>

<p className="mt-2 opacity-90">

Recommended AI case study based on your engineering level.

</p>

</div>

</div>



{/* Technology Dependencies */}

<div className="bg-white rounded-2xl shadow-lg p-6">

<h2 className="text-2xl font-bold flex items-center gap-2 mb-5">

<Cpu className="text-blue-600"/>

Technology Dependencies

</h2>

<div className="flex flex-wrap gap-3">

{roadmap.technology_dependencies.map((tech,index)=>(

<span
key={index}
className="px-4 py-2 rounded-full bg-blue-100 text-blue-700 font-semibold"
>

{tech}

</span>

))}

</div>

</div>
{/* Missing Skills */}

<div className="bg-white rounded-2xl shadow-lg p-6">

<h2 className="text-2xl font-bold flex items-center gap-2 mb-5">

<Sparkles className="text-red-600"/>

Missing Skills

</h2>

<div className="flex flex-wrap gap-3">

{roadmap.missing_skills.map((skill,index)=>(

<span
key={index}
className="px-4 py-2 rounded-full bg-red-100 text-red-700 font-semibold"
>

{skill}

</span>

))}

</div>

</div>



{/* Complete Roadmap */}

<div className="bg-white rounded-2xl shadow-lg p-6">

<h2 className="text-2xl font-bold flex items-center gap-2 mb-6">

<Map className="text-green-600"/>

Complete Roadmap

</h2>

<div className="space-y-5">

{roadmap.roadmap.map((step,index)=>(

<div
key={index}
className="flex items-start gap-4"
>

<div className="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold">

{index + 1}

</div>

<div className="flex-1 border-l-4 border-blue-300 pl-5 pb-6">

<h3 className="font-semibold text-lg">

{step}

</h3>

</div>

</div>

))}

</div>

</div>
{/* Estimated Graduation */}

<div className="bg-gradient-to-r from-green-500 to-emerald-600 text-white rounded-2xl shadow-lg p-6">

<div className="flex justify-between items-center">

<div>

<h2 className="text-2xl font-bold">

Estimated Graduation

</h2>

<p className="mt-2 text-lg">

{roadmap.estimated_graduation}

</p>

</div>

<TrendingUp size={60}/>

</div>

</div>


</div>

)}

</div>

</div>

</div>

</div>

);

}

export default Roadmap;