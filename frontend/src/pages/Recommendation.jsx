import React, { useEffect, useState } from "react";
import api from "../api/axios";

import {
    Brain,
    Target,
    BookOpen,
    Rocket,
    AlertCircle,
    Sparkles,
    CheckCircle,
    Award,
    TrendingUp,
    Activity,
    Code2,
    Users,
    FileCheck
} from "lucide-react";


function Recommendation() {

    const [students, setStudents] = useState([]);

    const [selectedStudent, setSelectedStudent] = useState("");

    const [form, setForm] = useState({
        attendance: 0,
        coding_speed: 0,
        interview_score: 0,
        case_study_score: 0,
        skills: [],
        skill_scores: []
    });

    const [result, setResult] = useState(null);

    const [loading, setLoading] = useState(false);

    const [loadingStudent, setLoadingStudent] = useState(false);

    const [error, setError] = useState("");


    // =========================================================
    // LOAD ALL STUDENTS
    // =========================================================

    useEffect(() => {

        loadStudents();

    }, []);


    async function loadStudents() {

        try {

            setError("");

            const response = await api.get(
                "/students/"
            );

            const studentList = response.data || [];

            setStudents(studentList);

            // Automatically select first student

            if (
                studentList.length > 0
                &&
                !selectedStudent
            ) {

                setSelectedStudent(
                    Number(studentList[0].id)
                );

            }

        } catch (error) {

            console.error(
                "Students loading error:",
                error.response?.data ||
                error.message
            );

            setError(
                "Unable to load students."
            );

        }

    }


    // =========================================================
    // LOAD SELECTED STUDENT PROFILE
    // =========================================================

    useEffect(() => {

        if (selectedStudent) {

            loadStudentProfile(
                selectedStudent
            );

        }

    }, [selectedStudent]);


    async function loadStudentProfile(
        studentId
    ) {

        try {

            setLoadingStudent(true);

            setError("");

            setResult(null);

            const response = await api.get(
                `/dashboard/student/${studentId}`
            );

            const student = response.data;

            const studentSkills =
                student.skills || [];


            // =================================================
            // LOAD ACTUAL STUDENT DATA
            // =================================================

            setForm({

                attendance:
                    Number(
                        student.attendance
                    ) || 0,

                coding_speed:
                    Number(
                        student.coding_speed
                    ) || 0,

                interview_score:
                    Number(
                        student.interview_score
                    ) || 0,

                case_study_score:
                    Number(
                        student.case_study_score
                    ) || 0,

                skills:
                    studentSkills.map(
                        skill => skill.name
                    ),

                skill_scores:
                    studentSkills.map(
                        skill =>
                            Number(
                                skill.score
                            ) || 0
                    )

            });

        } catch (error) {

            console.error(
                "Student profile error:",
                error.response?.data ||
                error.message
            );

            setError(
                error.response?.data?.detail ||
                "Unable to load student profile."
            );

        } finally {

            setLoadingStudent(false);

        }

    }


    // =========================================================
    // INPUT CHANGE
    // =========================================================

    function handleChange(
        field,
        value
    ) {

        setForm(prev => ({

            ...prev,

            [field]:
                Number(value)

        }));

    }


    // =========================================================
    // GENERATE RECOMMENDATION
    // =========================================================

    async function generateRecommendation() {

        if (!selectedStudent) {

            setError(
                "Please select a student first."
            );

            return;

        }


        try {

            setLoading(true);

            setResult(null);

            setError("");


            const payload = {

                attendance:
                    Number(
                        form.attendance
                    ),

                coding_speed:
                    Number(
                        form.coding_speed
                    ),

                interview_score:
                    Number(
                        form.interview_score
                    ),

                case_study_score:
                    Number(
                        form.case_study_score
                    ),

                skills:
                    form.skills,

                skill_scores:
                    form.skill_scores

            };


            console.log(
                "Recommendation Payload:",
                payload
            );


            const response =
                await api.post(
                    "/recommendations/",
                    payload
                );


            setResult(
                response.data
            );


        } catch (error) {

            console.error(
                "Recommendation error:",
                error.response?.data ||
                error.message
            );

            setError(

                error.response?.data?.detail

                    ? JSON.stringify(
                        error.response.data.detail
                    )

                    : "Unable to generate recommendation."

            );

        } finally {

            setLoading(false);

        }

    }


    return (

        <div className="
            min-h-screen
            bg-slate-100
            p-8
        ">


            {/* =================================================
                HEADER
            ================================================= */}

            <div className="
                bg-gradient-to-r
                from-blue-700
                to-indigo-700
                rounded-2xl
                p-6
                text-white
                mb-8
                shadow-lg
            ">

                <div className="
                    flex
                    items-center
                    gap-4
                ">

                    <Sparkles size={40} />

                    <div>

                        <h1 className="
                            text-3xl
                            font-bold
                        ">
                            AI Career Recommendation Engine
                        </h1>

                        <p className="
                            text-blue-100
                            mt-2
                        ">
                            AI powered career analysis based on
                            individual student performance
                        </p>

                    </div>

                </div>

            </div>


            {/* =================================================
                STUDENT SELECTOR
            ================================================= */}

            <div className="
                bg-white
                rounded-2xl
                shadow-md
                p-6
                mb-8
            ">

                <label className="
                    block
                    font-semibold
                    mb-2
                ">
                    Select Student
                </label>


                <select
                    value={selectedStudent}
                    onChange={(e) =>
                        setSelectedStudent(
                            Number(
                                e.target.value
                            )
                        )
                    }
                    disabled={
                        students.length === 0
                        ||
                        loadingStudent
                    }
                    className="
                        w-full
                        border
                        rounded-xl
                        p-3
                        outline-none
                        focus:ring-2
                        focus:ring-blue-500
                    "
                >

                    <option value="">
                        Select a student
                    </option>


                    {students.map(
                        student => (

                            <option
                                key={student.id}
                                value={student.id}
                            >

                                {student.name ||
                                    student.full_name ||
                                    `Student ${student.id}`}

                            </option>

                        )
                    )}

                </select>


                {loadingStudent && (

                    <p className="
                        text-blue-600
                        text-sm
                        mt-2
                    ">
                        Loading student profile...
                    </p>

                )}

            </div>


            <div className="
                grid
                lg:grid-cols-2
                gap-8
            ">


                {/* =================================================
                    EVALUATION
                ================================================= */}

                <div className="
                    bg-white
                    rounded-2xl
                    shadow-md
                    p-6
                ">

                    <h2 className="
                        text-xl
                        font-bold
                        mb-6
                        flex
                        items-center
                        gap-2
                    ">

                        <Activity className="
                            text-blue-600
                        " />

                        Student Evaluation Metrics

                    </h2>


                    <MetricInput
                        name="Attendance"
                        field="attendance"
                        value={form.attendance}
                        icon={<Users />}
                        onChange={handleChange}
                    />


                    <MetricInput
                        name="Coding Speed"
                        field="coding_speed"
                        value={form.coding_speed}
                        icon={<Code2 />}
                        onChange={handleChange}
                    />


                    <MetricInput
                        name="Interview Score"
                        field="interview_score"
                        value={form.interview_score}
                        icon={<Target />}
                        onChange={handleChange}
                    />


                    <MetricInput
                        name="Case Study Score"
                        field="case_study_score"
                        value={form.case_study_score}
                        icon={<FileCheck />}
                        onChange={handleChange}
                    />


                    {/* =================================================
                        CURRENT SKILLS
                    ================================================= */}

                    <div className="mt-6">

                        <h3 className="
                            font-bold
                            mb-3
                        ">
                            Current Skills
                        </h3>


                        {form.skills.length > 0 ? (

                            <div className="
                                flex
                                flex-wrap
                                gap-2
                            ">

                                {form.skills.map(
                                    (skill, index) => (

                                        <span
                                            key={index}
                                            className="
                                                bg-blue-100
                                                text-blue-700
                                                px-3
                                                py-2
                                                rounded-lg
                                                text-sm
                                                font-semibold
                                            "
                                        >

                                            {skill}

                                            {" "}

                                            (
                                            {
                                                form.skill_scores[
                                                    index
                                                ] || 0
                                            }%
                                            )

                                        </span>

                                    )
                                )}

                            </div>

                        ) : (

                            <p className="
                                text-gray-500
                            ">
                                No skills available for this student.
                            </p>

                        )}

                    </div>


                    {/* =================================================
                        ERROR
                    ================================================= */}

                    {error && (

                        <div className="
                            mt-5
                            bg-red-50
                            text-red-700
                            border
                            border-red-200
                            rounded-xl
                            p-4
                        ">

                            {error}

                        </div>

                    )}


                    {/* =================================================
                        GENERATE BUTTON
                    ================================================= */}

                    <button
                        onClick={
                            generateRecommendation
                        }
                        disabled={
                            loading ||
                            loadingStudent ||
                            !selectedStudent
                        }
                        className="
                            w-full
                            mt-6
                            bg-blue-600
                            hover:bg-blue-700
                            disabled:bg-blue-300
                            text-white
                            py-3
                            rounded-xl
                            font-bold
                            transition
                        "
                    >

                        {loading

                            ? "Analyzing Student Profile..."

                            : "Generate AI Recommendation"

                        }

                    </button>

                </div>


                {/* =================================================
                    RESULT
                ================================================= */}

                <div className="
                    bg-white
                    rounded-2xl
                    shadow-md
                    p-6
                ">

                    {result ? (

                        <>

                            <h2 className="
                                text-xl
                                font-bold
                                flex
                                items-center
                                gap-2
                                mb-6
                            ">

                                <Brain className="
                                    text-purple-600
                                " />

                                AI Analysis Result

                            </h2>


                            <div className="
                                grid
                                md:grid-cols-2
                                gap-4
                            ">


                                <Card
                                    title="Engineering Score"
                                    value={`${result.engineering_score ?? 0}%`}
                                    icon={<TrendingUp />}
                                />


                                <Card
                                    title="Engineering Level"
                                    value={
                                        result.engineering_level ||
                                        "Not Available"
                                    }
                                    icon={<Award />}
                                />


                                <Card
                                    title="Job Readiness"
                                    value={
                                        result.job_readiness ||
                                        "Not Available"
                                    }
                                    icon={<CheckCircle />}
                                />


                                <Card
                                    title="Promotion Readiness"
                                    value={
                                        result.promotion_readiness ||
                                        "Not Available"
                                    }
                                    icon={<Target />}
                                />


                                <Card
                                    title="Recommended Role"
                                    value={
                                        result.recommended_role ||
                                        "Not Available"
                                    }
                                    icon={<Rocket />}
                                />

                            </div>


                            <Section
                                title="Recommended Projects"
                                icon={<Rocket />}
                                items={
                                    result.recommended_projects ||
                                    []
                                }
                            />


                            <Section
                                title="Learning Priority"
                                icon={<BookOpen />}
                                items={
                                    result.learning_priority ||
                                    []
                                }
                            />


                            <Section
                                title="Missing Skills"
                                icon={<AlertCircle />}
                                items={
                                    result.missing_skills ||
                                    []
                                }
                            />

                        </>

                    ) : (

                        <div className="
                            h-full
                            min-h-[500px]
                            flex
                            flex-col
                            items-center
                            justify-center
                            text-gray-400
                            gap-3
                        ">

                            <Brain size={50} />

                            <p className="
                                text-lg
                                text-center
                            ">

                                Select a student and generate
                                AI recommendation.

                            </p>

                        </div>

                    )}

                </div>

            </div>

        </div>

    );

}


// =========================================================
// METRIC INPUT
// =========================================================

function MetricInput({
    name,
    field,
    value,
    icon,
    onChange
}) {

    return (

        <div className="mb-5">

            <div className="
                flex
                items-center
                gap-2
                font-semibold
                mb-2
            ">

                <span className="
                    text-blue-600
                ">

                    {icon}

                </span>

                {name}

            </div>


            <input
                type="number"
                min="0"
                max="100"
                value={value}
                onChange={(e) =>
                    onChange(
                        field,
                        e.target.value
                    )
                }
                className="
                    w-full
                    border
                    rounded-xl
                    p-3
                    focus:ring-2
                    focus:ring-blue-500
                    outline-none
                "
            />

        </div>

    );

}


// =========================================================
// CARD
// =========================================================

function Card({
    title,
    value,
    icon
}) {

    return (

        <div className="
            border
            rounded-xl
            p-5
            bg-slate-50
        ">

            <div className="
                flex
                justify-between
                items-center
            ">

                <div>

                    <p className="
                        text-gray-500
                        text-sm
                    ">
                        {title}
                    </p>


                    <h2 className="
                        text-xl
                        font-bold
                        mt-1
                    ">

                        {value || "N/A"}

                    </h2>

                </div>


                <div className="
                    text-blue-600
                ">

                    {icon}

                </div>

            </div>

        </div>

    );

}


// =========================================================
// SECTION
// =========================================================

function Section({
    title,
    icon,
    items = []
}) {

    return (

        <div className="
            mt-6
            bg-indigo-50
            rounded-xl
            p-5
        ">

            <h3 className="
                font-bold
                flex
                items-center
                gap-2
                mb-3
            ">

                {icon}

                {title}

            </h3>


            {items.length > 0 ? (

                items.map(
                    (item, index) => (

                        <div
                            key={index}
                            className="
                                bg-white
                                rounded-lg
                                p-3
                                mb-2
                                shadow-sm
                            "
                        >

                            {item}

                        </div>

                    )
                )

            ) : (

                <p className="
                    text-gray-500
                ">
                    No data available
                </p>

            )}

        </div>

    );

}


export default Recommendation;