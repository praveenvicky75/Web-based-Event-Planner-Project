import { useParams } from "react-router-dom";
import { useState } from "react";

function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("")
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log("Email:", email);
        console.log("Password:", password);
        alert(`Logged in with ${email}`);
    }
    const styles = {
        container: {
            width: "300px",
            margin: "100px auto",
            padding: "20px",
            border: "1px solid #ccc",
            borderRadius: "10px",
            textAlign: "center",
            boxShadow: "0px 4px 8px rgba(0,0,0,0.2)",
        },
        title: {
            marginBottom: "20px",
        },
        form: {
            display: "flex",
            flexDirection: "column",
        },
        input: {
            marginBottom: "15px",
            padding: "10px",
            borderRadius: "5px",
            border: "1px solid #ccc",
            fontSize: "14px",
        },
        button: {
            padding: "10px",
            backgroundColor: "#007bff",
            color: "white",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
        },
    }
    return (
        <>
            <div style={styles.container}>
                <h2 style={styles.title}>Login</h2>
                <form onSubmit={handleSubmit} style={styles.form}>
                    <input
                        type="email"
                        placeholder="Enter Email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        style={styles.input}
                        required
                    />
                    <input
                        type="password"
                        placeholder="Enter Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        style={styles.input}
                        required
                    />
                    <button type="submit" style={styles.button}>
                        Submit
                    </button>
                </form>
            </div>

        </>
    );
}

export default Login;