import {useContext, useEffect, useState, useRef} from "react";
import {Typography} from "@mui/material";
import Grid2 from '@mui/material/Unstable_Grid2';
import ReactMarkdown from 'react-markdown'

import {AppContext, UserContext} from "../App";
import * as util from "../util";

function Main() {
    const appContext = useContext(AppContext);
    const userContext = useContext(UserContext);

    const refFirstRef = useRef(true);

    const [docs, setDocs] = useState([]);

    useEffect(() => {
        if (import.meta.env.DEV && refFirstRef.current) {
            refFirstRef.current = false;
            return;
        }

        (async () => {
            appContext.backdrop.open();
            const config = {
                method: "get",
                url: "doc/docs"
            };
            try {
                const res = await util.request(config, userContext);
                setDocs(res.data);
            } catch (err) {
                appContext.completed.err(err);
            } finally {
                appContext.backdrop.close();
            }
        })();
    }, []);

    return (
        <Grid2 container spacing={2}>
            {docs.map((v, i) => (
                <Grid2 xs={4} key={i}>
                    <Typography>{v.filename}</Typography>
                    <ReactMarkdown>{v.content}</ReactMarkdown>
                    <Typography>{v.last_update}</Typography>
                </Grid2>
            ))}
        </Grid2>
    );
}

export default Main;
