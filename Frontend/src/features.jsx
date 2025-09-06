import { useNavigate } from 'react-router-dom';
import './features.css'
function Features(props){
    const navigate = useNavigate();
    const handleClick = ()=> {
        if(props.to){
            navigate(props.to);
        }
    };

    return( 
        <>
        <span className="box" onClick={handleClick}>
            <img src={props.img} />
            <p>{props.text}</p>

        </span>
        </>
    );
}

export default Features;