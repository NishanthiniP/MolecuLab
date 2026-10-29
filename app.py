
import streamlit as st

st.set_page_config(
    page_title="MolecuLab",
    page_icon="🧪",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: #f5f7fa;
}
[data-testid="stSidebar"] {
    background-color: #20232e;
}
h1, h2, h3 {
    color: #67e8f9;
}
</style>
""", unsafe_allow_html=True)

st.title("🧪 MolecuLab")
st.subheader("Your Virtual Chemistry Laboratory")

st.write(
    "Explore molecules, understand chemical structures, "
    "and learn computational chemistry interactively."
)

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📖 Theory",
        "🧬 Molecular Visualization",
        "📊 Molecular Properties",
        "📈 Structure–Property Analysis",
        "📝 Assessment",
        "📄 Final Project Report"
    ]
)

st.sidebar.divider()
st.sidebar.subheader("🎓 Student Information")

student = st.sidebar.text_input("Student Name")
register = st.sidebar.text_input("Registration Number")

if page == "🏠 Home":
    st.header("Welcome to MolecuLab!")
    st.write("Learn chemistry through interactive molecular exploration.")

    st.subheader("🧪 What can you do?")
    features = [
        "Enter SMILES notation",
        "Generate 2D molecular structures",
        "Explore 3D molecules",
        "Calculate molecular properties",
        "Compare different molecules",
        "Take chemistry assessments",
        "Prepare a final project report"
    ]

    for feature in features:
        st.write("✅ " + feature)

    st.subheader("🧫 Example Molecules")

    molecules = {
        "Ethanol": "CCO",
        "Benzene": "c1ccccc1",
        "Phenol": "Oc1ccccc1",
        "Acetic Acid": "CC(=O)O",
        "Aspirin": "CC(=O)Oc1ccccc1C(=O)O"
    }

    st.table([
        {"Molecule": name, "SMILES": smiles}
        for name, smiles in molecules.items()
    ])

elif page == "📖 Theory":
    st.header("📖 Chemistry Theory")
    st.markdown("""
    ### What is Chemoinformatics?
    Chemoinformatics uses computers to store, analyze,
    and understand chemical information.

    ### What is SMILES?
    SMILES represents a chemical structure using text.

    Examples:
    - Water: `O`
    - Ethanol: `CCO`
    - Benzene: `c1ccccc1`

    ### Applications
    - Drug discovery
    - Molecular modeling
    - Chemical database searching
    - Computational chemistry
    """)

elif page == "🧬 Molecular Visualization":
    st.header("🧬 Molecular Visualization")
    smiles = st.text_input(
        "Enter SMILES notation",
        placeholder="Example: CCO"
    )

    st.info(
        "2D and 3D structure generation will be added "
        "in the next development stage."
    )

    if smiles:
        st.write("Your input:", smiles)

elif page == "📊 Molecular Properties":
    st.header("📊 Molecular Properties")
    st.write(
        "Molecular weight, molecular formula, "
        "and other calculated properties will be added next."
    )

elif page == "📈 Structure–Property Analysis":
    st.header("📈 Structure–Property Analysis")
    st.write("Compare chemical structures and their properties.")

elif page == "📝 Assessment":
    st.header("📝 Chemistry Assessment")
    answer = st.radio(
        "Which notation represents ethanol?",
        ["CO", "CCO", "O=C=O", "c1ccccc1"]
    )

    if st.button("Check Answer"):
        if answer == "CCO":
            st.success("Correct! CCO represents ethanol.")
        else:
            st.error("Not quite. Try again!")

elif page == "📄 Final Project Report":
    st.header("📄 Final Project Report")

    if student:
        st.write("Student:", student)
    if register:
        st.write("Registration Number:", register)

    st.write("Project: MolecuLab Virtual Chemistry Laboratory")
    st.write("Topic: Chemoinformatics and Computational Chemistry")
