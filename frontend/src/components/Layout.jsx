import React from "react";
import { Link, Outlet } from "react-router-dom";

import {
    LayoutDashboard,
    User,
    BrainCircuit,
    Network,
    Map,
    BookOpen
} from "lucide-react";


function Layout(){

    return (

        <div className="flex min-h-screen bg-gray-100">


            {/* Sidebar */}

            <aside className="w-64 bg-white shadow-lg p-6">


                <h1 className="text-xl font-bold mb-8 text-blue-600">

                    AI Roadmap Engine

                </h1>



                <nav className="space-y-3">


                    <Menu
                    to="/"
                    icon={<LayoutDashboard size={18}/>}
                    text="Dashboard"
                    />


                    <Menu
                    to="/student/1"
                    icon={<User size={18}/>}
                    text="Student Profile"
                    />


                    <Menu
                    to="/recommendation"
                    icon={<BrainCircuit size={18}/>}
                    text="AI Recommendation"
                    />


                    <Menu
                    to="/skill-tree"
                    icon={<Network size={18}/>}
                    text="Skill Tree"
                    />


                    <Menu
                    to="/roadmap"
                    icon={<Map size={18}/>}
                    text="Roadmap"
                    />


                    <Menu
                    to="/case-studies"
                    icon={<BookOpen size={18}/>}
                    text="Case Studies"
                    />


                </nav>


            </aside>





            {/* Main Content */}

            <main className="flex-1">

                <Outlet/>

            </main>



        </div>

    )

}





function Menu({to,icon,text}){


    return (

        <Link

        to={to}

        className="flex items-center gap-3 p-3 rounded-lg hover:bg-blue-50 hover:text-blue-600 transition">


            {icon}

            <span>

                {text}

            </span>


        </Link>

    )

}


export default Layout;