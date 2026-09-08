import React, { useEffect, useState } from "react";
import api from "../api/axios";

import {
  Users,
  Brain,
  BookOpen,
  Award,
  TrendingUp,
  Target,
  User,
  Briefcase,
  CheckCircle,
  Search,
  Bell,
  Rocket,
  Cpu,
  Sparkles,
  AlertTriangle,
  GitBranch,
  Container,
  Code2,
} from "lucide-react";

import { motion } from "framer-motion";

import {
  ResponsiveContainer,
  RadarChart,
  Radar,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
} from "recharts";

import {
  CircularProgressbar,
  buildStyles,
} from "react-circular-progressbar";

import "react-circular-progressbar/dist/styles.css";


/* =========================================================
   INFO CARD
========================================================= */

function InfoCard({ icon, title, value }) {
  return (
    <div className="bg-slate-50 rounded-xl p-4">
      <div className="text-blue-600 mb-2">
        {icon}
      </div>

      <p className="text-gray-500 text-sm">
        {title}
      </p>

      <h3 className="font-bold mt-1">
        {value}
      </h3>
    </div>
  );
}


/* =========================================================
   STAT CARD
========================================================= */

function StatCard({ title, value, icon, color }) {
  return (
    <motion.div
      whileHover={{ y: -5 }}
      className="bg-white rounded-2xl shadow-lg p-6"
    >
      <div className="flex justify-between items-center">

        <div>
          <p className="text-gray-500">
            {title}
          </p>

          <h2 className="text-3xl font-bold mt-2">
            {value}
          </h2>
        </div>

        <div
          className={`h-14 w-14 rounded-xl flex items-center justify-center ${color}`}
        >
          {icon}
        </div>

      </div>
    </motion.div>
  );
}


/* =========================================================
   DASHBOARD
========================================================= */

export default function Dashboard() {

  const [stats, setStats] = useState({});
  const [student, setStudent] = useState({});
  const [radarData, setRadarData] = useState([]);

  const [loading, setLoading] = useState(true);


  /* =======================================================
     LOAD DASHBOARD
  ======================================================= */

  useEffect(() => {
    loadDashboard();
  }, []);


  async function loadDashboard() {

    try {

      setLoading(true);


      /* Overall dashboard */

      const dashboardResponse =
        await api.get("/dashboard");

      setStats(
        dashboardResponse.data || {}
      );


      /* Student dashboard */

      const studentResponse =
        await api.get("/dashboard/student/1");

      const studentData =
        studentResponse.data || {};

      setStudent(studentData);


      /* Dynamic radar data from backend */

      const backendSkills =
        studentData.skills || [];

      setRadarData(
        backendSkills.map((item) => ({
          skill: item.name,
          score: item.score,
        }))
      );


    } catch (error) {

      console.error(
        "Dashboard loading error:",
        error
      );

    } finally {

      setLoading(false);

    }
  }


  /* =======================================================
     VALUES FROM BACKEND
  ======================================================= */

  const engineeringScore =
    student.engineering_score || 0;


  const level =
    student.level || "Beginner";


  const readiness =
    student.job_readiness || "Learning";


  const careerPrediction =
    student.career_prediction || {};


  const careerRole =
    careerPrediction.role ||
    "AI Learner";


  const confidence =
    careerPrediction.confidence || 0;


  const skills =
    student.skills || [];


  const missingSkills =
    student.missing_skills || [];


  const roadmap =
    student.roadmap || [];


  const caseStudies =
    student.case_studies || [];


  /* =======================================================
     AI INSIGHTS - DYNAMIC
  ======================================================= */

  const aiInsights = [];


  skills.forEach((skill) => {

    if (skill.score >= 85) {

      aiInsights.push({
        text: `Excellent ${skill.name} Skills`,
        type: "success",
      });

    } else if (skill.score >= 75) {

      aiInsights.push({
        text: `Strong ${skill.name} Development`,
        type: "success",
      });

    } else {

      aiInsights.push({
        text: `Improve ${skill.name} Skills`,
        type: "warning",
      });

    }

  });


  /* Add missing skill insights */

  missingSkills.slice(0, 3).forEach((skill) => {

    aiInsights.push({
      text: `Learn ${skill}`,
      type: "warning",
    });

  });


  /* =======================================================
     RECOMMENDED PROJECTS
  ======================================================= */

  const recommendedProjects = [

    {
      title: "AI Chatbot",
      description:
        "Build an AI powered chatbot using Python and LLM technologies.",
    },

    {
      title: "RAG Question Answering",
      description:
        "Build a Retrieval Augmented Generation question answering system.",
    },

    {
      title: "AI Workflow Automation",
      description:
        "Build an AI powered workflow automation platform.",
    },

  ];


  /* =======================================================
     LOADING
  ======================================================= */

  if (loading) {

    return (
      <div className="min-h-screen bg-slate-100 flex items-center justify-center">

        <div className="text-center">

          <div className="animate-spin h-12 w-12 border-4 border-blue-600 border-t-transparent rounded-full mx-auto" />

          <p className="mt-4 text-gray-600">
            Loading AI Dashboard...
          </p>

        </div>

      </div>
    );

  }


  /* =======================================================
     UI
  ======================================================= */

  return (

    <div className="min-h-screen bg-slate-100">


      {/* ===================================================
          HEADER
      =================================================== */}

      <div className="bg-gradient-to-r from-blue-700 via-indigo-700 to-purple-700">

        <div className="max-w-7xl mx-auto px-8 py-6 flex justify-between">

          <div>

            <h1 className="text-4xl font-bold text-white">
              AI Internship Dashboard
            </h1>

            <p className="text-blue-100 mt-1">
              AI Powered Internship Analytics Platform
            </p>

          </div>


          <div className="flex gap-4 items-center">

            <div className="bg-white rounded-xl px-4 py-3 flex">

              <Search size={20} />

              <input
                className="ml-2 outline-none"
                placeholder="Search..."
              />

            </div>


            <button className="bg-white p-3 rounded-xl">

              <Bell />

            </button>


            <div className="bg-white rounded-full p-3">

              <User />

            </div>

          </div>

        </div>

      </div>


      {/* ===================================================
          MAIN
      =================================================== */}

      <div className="max-w-7xl mx-auto p-8">


        {/* =================================================
            STATISTICS
        ================================================= */}

        <div className="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-6">


          <StatCard
            title="Students"
            value={stats.total_students || 0}
            icon={<Users className="text-white" />}
            color="bg-blue-600"
          />


          <StatCard
            title="Skills"
            value={stats.total_skills || 0}
            icon={<Brain className="text-white" />}
            color="bg-purple-600"
          />


          <StatCard
            title="Case Studies"
            value={stats.total_case_studies || 0}
            icon={<BookOpen className="text-white" />}
            color="bg-green-600"
          />


          <StatCard
            title="Average Score"
            value={`${stats.average_engineering_score || 0}%`}
            icon={<Award className="text-white" />}
            color="bg-yellow-500"
          />


          <StatCard
            title="Job Ready"
            value={stats.job_ready_students || 0}
            icon={<Target className="text-white" />}
            color="bg-red-500"
          />


          <StatCard
            title="AI Growth"
            value={`${engineeringScore}%`}
            icon={<TrendingUp className="text-white" />}
            color="bg-indigo-600"
          />

        </div>


        {/* =================================================
            STUDENT OVERVIEW
        ================================================= */}

        <div className="grid lg:grid-cols-3 gap-8 mt-10">


          {/* STUDENT PROFILE */}

          <motion.div
            className="bg-white rounded-3xl shadow-lg p-8"
          >

            <div className="flex items-center gap-5">

              <div className="h-24 w-24 rounded-full bg-blue-600 flex items-center justify-center">

                <User
                  className="text-white"
                  size={40}
                />

              </div>


              <div>

                <h2 className="text-2xl font-bold">
                  {student.name || "Student"}
                </h2>

                <p className="text-gray-500">
                  {student.email || "No email"}
                </p>

              </div>

            </div>


            <div className="grid grid-cols-2 gap-4 mt-8">


              <InfoCard
                icon={<Award />}
                title="Level"
                value={level}
              />


              <InfoCard
                icon={<Briefcase />}
                title="Career"
                value={careerRole}
              />


              <InfoCard
                icon={<Target />}
                title="Confidence"
                value={`${confidence}%`}
              />


              <InfoCard
                icon={<CheckCircle />}
                title="Status"
                value={readiness}
              />

            </div>

          </motion.div>


          {/* ENGINEERING SCORE */}

          <motion.div
            className="bg-white rounded-3xl shadow-lg p-8 flex flex-col items-center justify-center"
          >

            <h2 className="text-2xl font-bold mb-8">
              Engineering Score
            </h2>


            <div className="w-56">

              <CircularProgressbar
                value={engineeringScore}
                text={`${engineeringScore}%`}
                styles={buildStyles({
                  pathColor: "#2563EB",
                  trailColor: "#DBEAFE",
                  textColor: "#1E3A8A",
                })}
              />

            </div>


            <span
              className={`mt-8 px-5 py-2 rounded-full font-semibold ${
                readiness === "Ready"
                  ? "bg-green-100 text-green-700"
                  : readiness === "Almost Ready"
                  ? "bg-yellow-100 text-yellow-700"
                  : "bg-blue-100 text-blue-700"
              }`}
            >
              {readiness}
            </span>


            <p className="mt-4 text-gray-500 text-center">
              AI evaluated engineering performance based on technical skills.
            </p>

          </motion.div>


          {/* CAREER PREDICTION */}

          <motion.div
            className="rounded-3xl shadow-lg p-8 bg-gradient-to-br from-indigo-700 to-purple-700 text-white"
          >

            <Rocket size={45} />

            <h2 className="text-3xl font-bold mt-5">
              AI Career Prediction
            </h2>


            <p className="mt-5">
              Recommended Career
            </p>


            <h3 className="text-2xl font-bold">
              {careerRole}
            </h3>


            <div className="mt-8">

              <div className="flex justify-between">

                <span>
                  Confidence
                </span>

                <span>
                  {confidence}%
                </span>

              </div>


              <div className="h-4 bg-white/20 rounded-full mt-3">

                <div
                  className="h-4 bg-white rounded-full"
                  style={{
                    width: `${confidence}%`,
                  }}
                />

              </div>

            </div>

          </motion.div>

        </div>


        {/* =================================================
            AI ANALYTICS
        ================================================= */}

        <div className="grid lg:grid-cols-2 gap-8 mt-10">


          {/* RADAR */}

          <motion.div
            className="bg-white rounded-3xl shadow-lg p-8"
          >

            <div className="flex gap-3 items-center mb-8">

              <Cpu className="text-blue-600" />

              <h2 className="text-2xl font-bold">
                AI Skill Analysis
              </h2>

            </div>


            {radarData.length > 0 ? (

              <ResponsiveContainer
                width="100%"
                height={320}
              >

                <RadarChart data={radarData}>

                  <PolarGrid />

                  <PolarAngleAxis
                    dataKey="skill"
                  />

                  <PolarRadiusAxis
                    domain={[0, 100]}
                  />

                  <Radar
                    dataKey="score"
                    stroke="#2563EB"
                    fill="#2563EB"
                    fillOpacity={0.5}
                  />

                </RadarChart>

              </ResponsiveContainer>

            ) : (

              <div className="h-80 flex items-center justify-center text-gray-500">
                No skill data available
              </div>

            )}

          </motion.div>


          {/* SKILL PROGRESS */}

          <motion.div
            className="bg-white rounded-3xl shadow-lg p-8"
          >

            <h2 className="text-2xl font-bold mb-8">
              Skill Progress
            </h2>


            {skills.length > 0 ? (

              skills.map((item, index) => (

                <div
                  key={index}
                  className="mb-6"
                >

                  <div className="flex justify-between">

                    <span className="font-semibold">
                      {item.name}
                    </span>

                    <span className="text-blue-600 font-bold">
                      {item.score}%
                    </span>

                  </div>


                  <div className="h-3 bg-gray-200 rounded-full mt-2">

                    <div
                      className="h-3 bg-blue-600 rounded-full"
                      style={{
                        width: `${item.score}%`,
                      }}
                    />

                  </div>

                </div>

              ))

            ) : (

              <p className="text-gray-500">
                No skills found.
              </p>

            )}

          </motion.div>

        </div>


        {/* =================================================
            AI INSIGHTS
        ================================================= */}

        <div className="grid lg:grid-cols-2 gap-8 mt-10">


          {/* INSIGHTS */}

          <motion.div
            className="bg-white rounded-3xl shadow-lg p-8"
          >

            <div className="flex gap-3 mb-8">

              <Sparkles className="text-purple-600" />

              <h2 className="text-2xl font-bold">
                AI Insights
              </h2>

            </div>


            <div className="space-y-5">

              {aiInsights.length > 0 ? (

                aiInsights.slice(0, 8).map(
                  (insight, index) => (

                    <p
                      key={index}
                      className={`flex gap-3 ${
                        insight.type === "success"
                          ? "text-green-600"
                          : "text-orange-600"
                      }`}
                    >

                      {insight.type === "success" ? (
                        <CheckCircle />
                      ) : (
                        <AlertTriangle />
                      )}

                      {insight.text}

                    </p>

                  )
                )

              ) : (

                <p className="text-gray-500">
                  No AI insights available.
                </p>

              )}

            </div>

          </motion.div>


          {/* MISSING SKILLS */}

          <motion.div
            className="bg-white rounded-3xl shadow-lg p-8"
          >

            <h2 className="text-2xl font-bold mb-8">
              Missing Skills Priority
            </h2>


            {missingSkills.length > 0 ? (

              missingSkills.map(
                (skill, index) => (

                  <div
                    key={index}
                    className="bg-red-50 rounded-xl p-4 mb-4 flex justify-between"
                  >

                    <span className="font-semibold">
                      {skill}
                    </span>

                    <span className="text-red-600 font-semibold">
                      High
                    </span>

                  </div>

                )
              )

            ) : (

              <div className="bg-green-50 text-green-700 p-4 rounded-xl">
                No major missing skills detected.
              </div>

            )}

          </motion.div>

        </div>


        {/* =================================================
            PROJECTS
        ================================================= */}

        <div className="mt-12">

          <h2 className="text-3xl font-bold mb-8">
            Recommended AI Projects
          </h2>


          <div className="grid lg:grid-cols-3 gap-8">

            {recommendedProjects.map(
              (project, index) => (

                <motion.div
                  key={index}
                  whileHover={{ y: -5 }}
                  className="bg-white rounded-3xl shadow-lg p-7"
                >

                  <Rocket className="text-blue-600" />


                  <h3 className="text-xl font-bold mt-5">
                    {project.title}
                  </h3>


                  <p className="text-gray-500 mt-3">
                    {project.description}
                  </p>


                  <button
                    className="mt-5 bg-blue-600 text-white px-5 py-2 rounded-lg hover:bg-blue-700"
                  >
                    Start Project
                  </button>

                </motion.div>

              )
            )}

          </div>

        </div>


        {/* =================================================
            CASE STUDIES
        ================================================= */}

        <div className="mt-12">

          <h2 className="text-3xl font-bold mb-8">
            Student Case Studies
          </h2>


          {caseStudies.length > 0 ? (

            <div className="grid lg:grid-cols-2 gap-6">

              {caseStudies.map(
                (caseStudy, index) => (

                  <div
                    key={index}
                    className="bg-white rounded-2xl shadow-lg p-6"
                  >

                    <div className="flex justify-between">

                      <h3 className="text-xl font-bold">
                        {caseStudy.title}
                      </h3>

                      <span className="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm">
                        {caseStudy.status}
                      </span>

                    </div>


                    <div className="grid grid-cols-3 gap-4 mt-5">

                      <div>
                        <p className="text-gray-500 text-sm">
                          Technology
                        </p>

                        <p className="font-semibold">
                          {caseStudy.technology}
                        </p>
                      </div>


                      <div>
                        <p className="text-gray-500 text-sm">
                          Difficulty
                        </p>

                        <p className="font-semibold">
                          {caseStudy.difficulty}
                        </p>
                      </div>


                      <div>
                        <p className="text-gray-500 text-sm">
                          Score
                        </p>

                        <p className="font-semibold">
                          {caseStudy.score ?? 0}%
                        </p>
                      </div>

                    </div>

                  </div>

                )
              )}

            </div>

          ) : (

            <div className="bg-white rounded-2xl shadow-lg p-8 text-gray-500">
              No case studies available for this student.
            </div>

          )}

        </div>


        {/* =================================================
            ROADMAP
        ================================================= */}

        <div className="mt-12 bg-white rounded-3xl shadow-lg p-8">

          <h2 className="text-3xl font-bold mb-8">
            AI Internship Roadmap
          </h2>


          {roadmap.length > 0 ? (

            roadmap.map(
              (item, index) => (

                <div
                  key={index}
                  className="flex gap-5 mb-6"
                >

                  <div className="h-10 w-10 min-w-10 rounded-full bg-blue-600 text-white flex items-center justify-center">

                    {index + 1}

                  </div>


                  <div>

                    <h3 className="font-bold">
                      {item.week || `Week ${index + 1}`}
                      {" - "}
                      {item.title || item}
                    </h3>


                    <p className="text-gray-500">
                      Complete objectives and upload project on GitHub.
                    </p>

                  </div>

                </div>

              )
            )

          ) : (

            <p className="text-gray-500">
              No roadmap available.
            </p>

          )}

        </div>


        {/* =================================================
            LEARNING FOCUS
        ================================================= */}

        {student.learning_focus &&
          student.learning_focus.length > 0 && (

            <div className="mt-12">

              <h2 className="text-3xl font-bold mb-8">
                AI Learning Focus
              </h2>


              <div className="grid md:grid-cols-2 lg:grid-cols-5 gap-5">

                {student.learning_focus.map(
                  (item, index) => (

                    <div
                      key={index}
                      className="bg-white rounded-2xl shadow-md p-5"
                    >

                      <Code2 className="text-blue-600 mb-3" />

                      <h3 className="font-bold">
                        {item}
                      </h3>

                      <p className="text-gray-500 text-sm mt-2">
                        Recommended learning focus based on your engineering profile.
                      </p>

                    </div>

                  )
                )}

              </div>

            </div>

          )}


        {/* =================================================
            FOOTER
        ================================================= */}

        <footer className="mt-16 py-10 text-center border-t text-gray-500">

          <h2 className="text-xl font-bold text-gray-700">
            AI Internship Roadmap Generator
          </h2>


          <p className="mt-2">
            AI Powered Dynamic Skill Tree & Internship Analytics Platform
          </p>


          <p className="mt-5">
            © 2026 All Rights Reserved
          </p>

        </footer>

      </div>

    </div>

  );
}