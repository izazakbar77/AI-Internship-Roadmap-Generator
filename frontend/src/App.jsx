import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./components/Layout";

import Dashboard from "./pages/Dashboard";
import StudentProfile from "./pages/StudentProfile";
import Recommendation from "./pages/Recommendation";
import SkillTree from "./pages/SkillTree";
import Roadmap from "./pages/Roadmap";
import CaseStudies from "./pages/CaseStudies";


function App(){

return (

<BrowserRouter>

<Routes>


<Route element={<Layout/>}>


<Route 
path="/" 
element={<Dashboard/>}
/>


<Route 
path="/student/:id" 
element={<StudentProfile/>}
/>


<Route 
path="/recommendation" 
element={<Recommendation/>}
/>


<Route 
path="/skill-tree" 
element={<SkillTree/>}
/>


<Route 
path="/roadmap" 
element={<Roadmap/>}
/>


<Route 
path="/case-studies" 
element={<CaseStudies/>}
/>


</Route>


</Routes>


</BrowserRouter>

)

}


export default App;