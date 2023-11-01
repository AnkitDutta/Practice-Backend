const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 5000;

// app.use(logger);

// function logger(req, res, next){
//     next();
//     console.log("All Requests finished executing");
// }
// function auth(req, res, next) {
//     if(req.query.admin === 'true')
//         next()
//     else
//         res.send("No auth")
// }

// app.get('/users', (req, res)=>{
//     console.log("Users page");
//     res.send("User's Page");
// })

app.get('/getNames' , async (req, res) => {
    try {
        const response = [];
        for(let i = 1; i <= 5; i++){
            const res = await axios.get(`https://swapi.dev/api/people/${i}`);
            response.push(res.data);
        }
        console.log(response);
        res.send(response);
    } catch (error) {
        console.log(error);
    }
})


app.listen(PORT, ()=>{
    console.log(`PORT RUNNNING ON PORT ${PORT}`);
});