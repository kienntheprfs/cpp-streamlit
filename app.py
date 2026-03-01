from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, PlainTextResponse
import subprocess
import shutil
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def main_form():
    return """
    <html>
        <body>
            <h2>Upload your C++ function and test files</h2>
            <form action="/run" enctype="multipart/form-data" method="post">
                Function file (.cpp): <input name="func_file" type="file"><br>
                Test file (.cpp): <input name="test_file" type="file"><br>
                <input type="submit">
            </form>
        </body>
    </html>
    """

@app.post("/run")
def run_cpp(
    func_file: UploadFile = File(...),
    test_file: UploadFile = File(...)
):
    func_path = "uploaded_func.cpp"
    test_path = "uploaded_test.cpp"
    exe_path = "test_binary"
    # Save both files
    with open(func_path, "wb") as f:
        shutil.copyfileobj(func_file.file, f)
    with open(test_path, "wb") as f:
        shutil.copyfileobj(test_file.file, f)
    # Compile
    compile_cmd = ["g++", test_path, func_path, "-o", exe_path]
    try:
        compile_proc = subprocess.run(compile_cmd, capture_output=True, timeout=10)
        if compile_proc.returncode != 0:
            output = "Compilation failed:\n" + compile_proc.stderr.decode()
        else:
            run_proc = subprocess.run([f"./{exe_path}"], capture_output=True, timeout=5)
            output = run_proc.stdout.decode() + run_proc.stderr.decode()
    except Exception as e:
        output = f"Error: {e}"
    finally:
        for path in [func_path, test_path, exe_path]:
            if os.path.exists(path):
                os.remove(path)
    return PlainTextResponse(output)
