import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './info.css';

function Info() {
    // make the same but with hooks
    const [name, setName] = useState('');
    const [email, setEmail] = useState();
    const [rut, setRut] = useState();
    const [region, setRegion] = useState();
    const [group, setGroup] = useState();
    const [position, setPosition] = useState();


    const { postId } = useParams();
    // http://localhost:3000/Sebastian_Diaz&sdiazdelafuente9@gmail.com&17.856.856-2&Región_Metropolitana,_Comuna_de_San_Joaquin&Cuerpo_de_Bomberos_de_San_Joaquin&Bombero
    console.log(postId);

    useEffect(() => {
        // the following will take the id and create variables acording to the id
        // first we split the id the & and take the second part
        const info = postId.split('&');
        // make a loop to take the info and create variables
        for (let i = 0; i < info.length; i++) {
            if (i === 0) {
                for (let j = 0; j < info[i].length; j++) {
                    if (info[i][j] === '_') {
                        info[i] = info[i].replace('_', ' ');
                    }
                }
                setName(info[i]);
            }
            if (i === 1) {
                setEmail(info[i]);
            }
            if (i === 2) {
                setRut(info[i]);
            }
            if (i === 3) {
                for (let j = 0; j < info[i].length; j++) {
                    if (info[i][j] === '_') {
                        info[i] = info[i].replace('_', ' ');
                    }
                }
                setRegion(info[i]);
            }
            if (i === 4) {
                for (let j = 0; j < info[i].length; j++) {
                    if (info[i][j] === '_') {
                        info[i] = info[i].replace('_', ' ');
                    }
                }
                setGroup(info[i]);
            }
            if (i === 5) {
                for (let j = 0; j < info[i].length; j++) {
                    if (info[i][j] === '_') {
                        info[i] = info[i].replace('_', ' ');
                    }
                }
                setPosition(info[i]);
            }
        }
    }, [postId]);

    return (
        <div className="App">
            <header className="App-header">
                <div className='main-container'>
                    {/* <h1>Evento</h1> */}
                    <div className='img-container'>
                        <img src="https://fibom.cl/wp-content/uploads/2021/11/fibom-logo-blanco.png" alt="logo" />
                    </div>
                    <h3>Has sido registrado con éxito ¡Ya puedes ingresar!</h3>
                    <div className='info'>

                        {/* create a list that contains all the info of the fireman */}
                        <ul>
                            <li><span>{name}</span></li>
                            <li><span>{email}</span></li>
                            <li><span>{rut}</span></li>

                        </ul>
                    </div>
                </div>
            </header>
        </div>
    );
}

export default Info;
