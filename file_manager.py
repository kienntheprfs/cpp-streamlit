import streamlit as st
import os
import subprocess
import uuid

WORKSPACE = "."  # Current directory, change if needed

st.title("C++ Test & Function File Manager")

# Helper to list files by extension
def list_files(ext):
    return [f for f in os.listdir(WORKSPACE) if f.endswith(ext)]

# --- List and select files ---
st.header("Function Files (.cpp)")
func_files = list_files(".cpp")
func_file = st.selectbox("Select a function file to view/edit/delete:", func_files, key="func")

# --- CRUD for function file ---
with st.expander(f"Edit Function File: {func_file}", expanded=False):
    if func_file:
        with open(func_file, "r", encoding="utf-8") as f:
            func_content = f.read()
        new_func_content = st.text_area("Function file content", func_content, height=200, key="func_content")
        if st.button("Save Function File"):
            with open(func_file, "w", encoding="utf-8") as f:
                f.write(new_func_content)
            st.success(f"Saved {func_file}")
        if st.button("Delete Function File"):
            os.remove(func_file)
            st.warning(f"Deleted {func_file}")
            st.experimental_rerun()

st.header("Test Files (.cpp)")
test_files = list_files(".cpp")
test_file = st.selectbox("Select a test file to view/edit/delete:", test_files, key="test")

# --- CRUD for test file ---
with st.expander(f"Edit Test File: {test_file}", expanded=False):
    if test_file:
        with open(test_file, "r", encoding="utf-8") as f:
            test_content = f.read()
        new_test_content = st.text_area("Test file content", test_content, height=200, key="test_content")
        if st.button("Save Test File"):
            with open(test_file, "w", encoding="utf-8") as f:
                f.write(new_test_content)
            st.success(f"Saved {test_file}")
        if st.button("Delete Test File"):
            os.remove(test_file)
            st.warning(f"Deleted {test_file}")
            st.experimental_rerun()

# --- Create new files ---
st.header("Create New File")
file_type = st.radio("File type:", ["Function", "Test"], horizontal=True)
if file_type == "Function":
    file_suffix = "_func.cpp"
else:
    file_suffix = "_test.cpp"
new_file_name = st.text_input("New file name (without extension):")
new_file_content = st.text_area("New file content", "", height=100)
if st.button("Create File"):
    if new_file_name:
        full_file_name = new_file_name + file_suffix
        with open(full_file_name, "w", encoding="utf-8") as f:
            f.write(new_file_content)
        st.success(f"Created {full_file_name}")
        st.experimental_rerun()
    else:
        st.error("Please enter a valid file name.")

# --- Upload and Run C++ Test ---
st.header("Upload and Run C++ Test")
func_file_upload = st.file_uploader("Upload function file (.cpp)", type=["cpp"], key="func_upload")
test_file_upload = st.file_uploader("Upload test file (.cpp)", type=["cpp"], key="test_upload")

st.markdown("**Or select from existing files:**")
existing_func = st.selectbox("Select existing function file:", ["(None)"] + func_files, key="run_func")
existing_test = st.selectbox("Select existing test file:", ["(None)"] + test_files, key="run_test")

if st.button("Compile and Run Test"):
    # Priority: uploaded files > selected files
    use_uploaded = func_file_upload is not None and test_file_upload is not None
    use_existing = existing_func != "(None)" and existing_test != "(None)"
    unique_id = str(uuid.uuid4())
    if use_uploaded:
        func_bytes = func_file_upload.getvalue()
        test_bytes = test_file_upload.getvalue()
        func_path = f"uploaded_func_{unique_id}.cpp"
        test_path = f"uploaded_test_{unique_id}.cpp"
        exe_path = f"test_binary_{unique_id}"
        with open(func_path, "wb") as f:
            f.write(func_bytes)
        with open(test_path, "wb") as f:
            f.write(test_bytes)
    elif use_existing:
        func_path = existing_func
        test_path = existing_test
        exe_path = f"test_binary_{unique_id}"
    else:
        st.warning("Please upload or select both a function file and a test file.")
        st.stop()
    # Compile
    compile_cmd = ["g++", test_path, func_path, "-o", exe_path]
    try:
        compile_proc = subprocess.run(compile_cmd, capture_output=True, timeout=10)
        if compile_proc.returncode != 0:
            st.error("Compilation failed:\n" + compile_proc.stderr.decode())
        else:
            run_proc = subprocess.run([f"./{exe_path}"], capture_output=True, timeout=5)
            st.success("Output:\n" + run_proc.stdout.decode() + run_proc.stderr.decode())
    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        # Only remove temp files if they were created
        if use_uploaded:
            for path in [func_path, test_path, exe_path]:
                if os.path.exists(path):
                    os.remove(path)
        elif use_existing:
            if os.path.exists(exe_path):
                os.remove(exe_path)
