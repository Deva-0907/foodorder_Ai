import streamlit as st

from agents.customer_agent import CustomerAgent
from agents.recommendation_agent import RecommendationAgent
from agents.restaurant_agent import RestaurantAgent
from agents.order_agent import OrderAgent


customer = CustomerAgent()
recommendation = RecommendationAgent()
restaurant = RestaurantAgent()
order = OrderAgent()


st.title("😋 Foodorder AI")
st.subheader("Multi-Agent Food Ordering Assistant")


user_input = st.text_input(
    "What would you like to eat?"
)


if st.button("Find Food"):

    if user_input.strip():

        with st.spinner("Customer Agent Working..."):
            customer_details = customer.understand_customer(user_input)

        st.success("Customer Agent Finished")

        st.write(customer_details)

        menu = restaurant.check_menu()

        with st.spinner("Recommendation Agent Working..."):
            food = recommendation.recommend(customer_details)

        st.success("Recommendation Ready")

        st.write(food)

        with st.spinner("Order Agent Creating Order..."):
            summary = order.create_order(food)

        st.success("Order Created")

        st.markdown("## Final Order")

        st.write(summary)