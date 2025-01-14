-- TRABAJO PRÁCTICO 01 - lenguaje de consultas SQL --

-- Punto1 y 2

use sakila;

SELECT  a.actor_id,
		a.first_name,
		a.last_name,
		a.last_update,
		fa.actor_id,
		fa.film_id,
		fa.last_update,
        f.description,
        f.release_year,
        f.language_id,
        f.original_language_id,
        f.rental_duration,
        f.rental_rate,
        f.replacement_cost,
        f.rating,
        f.length,
        f.special_features,
        f.last_update
        FROM actor a,
			film_actor fa,
            film f
INNER JOIN film_actor, film
WHERE a.actor_id = fa.actor_id
AND fa.film_id = f.film_id;


SELECT 	ad.address_id,
		ad.address,
        ad.district,
        ad.city_id,
        ad.postal_code,
        ad.phone,
        ad.location,
        ad.last_update,
        cu.address_id,
        cu.customer_id,
        cu.last_update
        FROM address ad,
			customer cu
INNER JOIN customer
WHERE ad.address_id=cu.address_id;


SELECT 	co.country_id,
		co.country,
        co.last_update,
        ci.city_id,
        ci.country_id,
        ci.last_update
 FROM 	country co,
		city ci
INNER JOIN city
WHERE co.country_id=ci.country_id;


SELECT	cu.customer_id,
		cu.store_id,
        cu.first_name,
        cu.last_name,
        cu.email,
        cu.last_update,
        st.store_id,
        st.last_update
		FROM customer cu,
			 store st
INNER JOIN store
WHERE cu.store_id=st.store_id;


SELECT  fa.actor_id,
		fa.film_id,
		fa.last_update,
        a.actor_id,
        a.last_update
        FROM film_actor fa,
			 actor a
INNER JOIN actor
WHERE fa.actor_id=a.actor_id;


SELECT 	fc.film_id,
		fc.category_id,
        fc.last_update,
        fm.film_id,
        fm.last_update
		FROM film_category fc,
			 film fm
INNER JOIN film
WHERE fc.film_id=fm.film_id;


SELECT 	ft.film_id,
		ft.title,
        ft.description,
        f.film_id,
        f.last_update
		FROM film_text ft,
			 film f
INNER JOIN film
WHERE ft.film_id=f.film_id;


SELECT 	inv.inventory_id,
		inv.film_id,
        inv.store_id,
        inv.last_update,
        st.store_id,
        st.last_update
		FROM 	inventory inv,
				store st
INNER JOIN store
WHERE inv.store_id=st.store_id;


SELECT ln.language_id,
		ln.name,
        ln.last_update,
        f.film_id,
        f.language_id,
        f.last_update
		FROM language ln,
			 film f
INNER JOIN film
WHERE ln.language_id=f.language_id;


SELECT 	pay.payment_id,
		pay.amount,
        pay.payment_date,
        pay.last_update
		FROM payment pay,
			 staff st
INNER JOIN staff
WHERE pay.staff_id=st.staff_id;


SELECT re.rental_id,
		re.inventory_id,
        re.return_date,
        re.last_update,
        inv.inventory_id,
        inv.last_update
		FROM rental re,
			 inventory inv
INNER JOIN inventory
WHERE re.inventory_id=inv.inventory_id;


SELECT  sta.staff_id,
		sta.first_name,
        sta.last_name,
        sta.address_id,
        sta.picture,
        sta.email,
        sta.store_id,
        sta.username,
        sta.last_update

		FROM staff sta,
			 store st
INNER JOIN store
WHERE sta.store_id=st.store_id;


SELECT  st.store_id,
		st.address_id,
        st.last_update,
        ad.address_id,
        ad.address,
        ad.district,
        ad.postal_code,
        ad.phone,
        ad.location,
        ad.last_update
		FROM store st,
			 address ad
INNER JOIN address
WHERE st.address_id=ad.address_id;


-- punto 3

-- Realizamos una suma

select p.staff_id "Staff",
	year(payment_date) "año",
    sum(amount)
from payment p,
	 staff s
where p.staff_id = s.staff_id
group by p.staff_id, year(payment_date);

-- Realizamos una consulta de año y mes

SELECT 	YEAR(payment_date)"año",
		MONTH(payment_date) "mes",
            min(amount)
from payment p
group by year(payment_date),month(payment_date);


-- Realizamos las siguientes consultas de los pagos: el monto mínimo pagado, el monto máximo pagado, el promedio del momnto de los pagos y la suma total del monto

select year(payment_date),
	r.rental_id,
    min(amount),
    max(amount),
    avg(amount),
    sum(amount)
from payment p,
	rental r
where r.rental_id = p.rental_id
group by year(payment_date);


-- Punto 4: hay 200 actores registrados

SELECT a.actor_id "Actores",
        concat(a.first_name,'  ',a.last_name) full_name
from actor a,
	 film_actor fa
WHERE a.actor_id=fa.actor_id
group by a.actor_id, year(full_name);


-- Punto 5:

SELECT 	p.rental_id "ID ALQUILER",
        p.amount "MONTO",
        p.rental_id "ID ALQUILER",
        r.inventory_id "ID INVENTARIO",
        i.inventory_id,
        i.film_id "ID FILM",
        f.film_id,
        f.title "TITULO",
        sum(p.amount) "TOTAL"
FROM	payment p,
		rental r,
        inventory i,
        film f
WHERE p.rental_id=r.rental_id
AND i.inventory_id=r.inventory_id
AND i.film_id=f.film_id
GROUP BY p.amount
order by 1 desc;
