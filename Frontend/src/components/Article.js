import React from 'react';
import { List, Typography } from 'antd';


const Articles = (props) => {
    return(
    <List
      header={<div>Texts</div>}
      footer={<div>From the channel</div>}
      bordered
      dataSource={props.data}
      renderItem={item => (
        <List.Item>
            {item.text}
        </List.Item>
      )}
    />
    );
}

export default Articles;