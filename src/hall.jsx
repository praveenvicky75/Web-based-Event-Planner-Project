import { useParams } from "react-router-dom";
import ABChall from './assets/ABChall.jpeg'
function Hall(){
    const {slug} = useParams();
    const styles = {
            container :{
                    border : "1px solid black",
                    backDrop:"blur(10)",
                    boxShadow: "0 8px 16px rgba(0,0,0,0.3)",
                    margin :"50px auto",
                    width :"50%",
                    textAlign:"center"
                    },
            img :{
                minHeight : "200px",
                paddingLeft : "10%"
            }
    }
    return(
        <>
        <div style={styles.container}>
            <h1 style={styles.text}>{slug.toUpperCase()} </h1>
            <p>Welcome to {slug} pre-booking page</p>
        </div>
        </>
    );
}
export default Hall;