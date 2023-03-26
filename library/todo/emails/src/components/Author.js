import React from'react'
import {Link} from 'react-router-dom'



const AuthorItem = ({item}) => {
    return(
        <tr>
            <td><Linkto={`author/${item.id}`}>{item.id}</Link></td>
            <td>{item.name}</td>
            <td>{item.birthday_year}</td> </tr>
    )
}

const AuthorList = ({items}) => {
    return(
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>BIRTHDAY_YEAR</th>
            </tr>
            {items.map((item) => <AuthorItemitem={item}/>)}
        </table>
    )
}
export default AuthorList
