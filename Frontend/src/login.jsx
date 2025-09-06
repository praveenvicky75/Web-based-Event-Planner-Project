import { useParams } from "react-router-dom";

function Login(){
    const styles = {
        box :{
            border :"20px solid black",
            borderRadius :"2px",
        },
    }
    return(
        <>
            <div className="loginBox" style={styles.box}>
                EmailID  : <input type="text" />
                Password : <input type="password" />
            </div>
        
        </>
    );
}

export default  Login;