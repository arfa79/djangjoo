from django.shortcuts import render
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Property
from .forms import TicketForm

def scrape_tickets(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            start_location = form.cleaned_data['start_location']
            destination_location = form.cleaned_data['destination_location']
            flying_date = form.cleaned_data['flying_date']

            # Construct the URL for alibaba.ir with user inputs
            url = f"https://www.alibaba.ir/tickets?start_location={start_location}&destination_location={destination_location}&flying_date={flying_date}"

            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                start_location=start_location,
                destination_location=destination_location,
                flying_date=flying_date,
                landing_date=landing_date,
                airline_company=airline_company,
                price=price,
                status=status,
                category=category,

                # Save the scraped data to the Ticket model
                ticket = Property.objects.create(
                    start_location=start_location,
                    destination_location=destination_location,
                    flying_date=flying_date,
                    landing_date=landing_date,
                    airline_company=airline_company,
                    price=price,
                    status=status,
                    category=category,
                )
                ticket.save()

                # Query the database to retrieve the tickets
                tickets = Property.objects.all()

                return render(request, 'tickets_table.html', {'tickets': tickets})

            except Exception as e:
                # Handle any exceptions that may occur during scraping
                error_message = str(e)
                return render(request, 'error.html', {'error_message': error_message})

    else:
        form = TicketForm()

    return render(request, 'ticket_table.html', {'form': form})

