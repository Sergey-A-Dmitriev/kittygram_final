import React from "react";
import { Link } from "react-router-dom";

import defaultImg from "../../images/default-kitty.jpg";

import styles from "./main-card.module.css";

export const MainCard = ({
  cardId,
  name = "",
  date = "",
  age = "",
  color = "Бежевый",
  img,
  extraClass = "",
}) => {
  const colorText =
    color === "black" ||
    color === "saddlebrown" ||
    color === "gray" ||
    color === "darkgray"
      ? "white"
      : "primary";

  return (
    <article className={`${styles.content} ${extraClass}`}>
      <Link className={styles.link} to={`/cats/${cardId}`}>
        <img
          className={styles.img}
          src={img ?? defaultImg}
          alt="Фото котика."
        />
      </Link>
      <div className={styles.data_box}>
        <div className={styles.name_n_date_box}>
          <p
            className={`text text_type_h3 text_color_primary mt-8 mb-3 ${styles.name}`}
          >
            {name}
          </p>
          <p
            className={`text text_type_medium-20 text_color_secondary mb-8 ${styles.date}`}
          >
            {date}
          </p>
          <p className={`text text_type_medium-20 text_color_secondary mb-8`}>
            Возраст: {age} {age === 1 ? 'год' : (age >= 2 && age <= 4 ? 'года' : 'лет')}
          </p>
        </div>
        <div
          className={styles.cat_color_box}
          style={{ backgroundColor: color }}
        >
          <p
            className={`text text_type_medium-20 text_color_${colorText} ${styles.cat_color}`}
          >
            {color}
          </p>
        </div>
      </div>
    </article>
  );
};
