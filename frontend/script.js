async function analyze() {
    try {
        const tasks = JSON.parse(document.getElementById("taskInput").value);
        const mode = document.getElementById("mode").value;

        const res = await fetch("http://127.0.0.1:8000/api/tasks/analyze/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ tasks, mode })
        });

        const data = await res.json();

        document.getElementById("output").innerHTML =
            `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    } catch (err) {
        document.getElementById("output").innerHTML =
            `<pre style="color:red;">Error: ${err}</pre>`;
    }
}
