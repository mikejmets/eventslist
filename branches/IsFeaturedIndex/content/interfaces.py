# -*- coding: utf-8 -*-

from zope.interface import Interface

##code-section HEAD
##/code-section HEAD

class IELEvent(Interface):
    """Marker interface for .elevent.ELEvent
    """

class IBooking(Interface):
    """Marker interface for .booking.Booking
    """

class IExternalEvent(Interface):
    """Marker interface for .externalevent.ExternalEvent
    """

class IPayment(Interface):
    """Marker interface for .payment.Payment
    """

class IPackage(Interface):
    """Marker interface for .package.Package
    """

class IELFolder(Interface):
    """Marker interface for .elfolder.ELFolder
    """

class IAgendaItem(Interface):
    """Marker interface for .agendaitem.AgendaItem
    """

class IInternalEvent(Interface):
    """Marker interface for .internalevent.InternalEvent
    """

class IEventAttendance(Interface):
    """Marker interface for .eventattendance.EventAttendance
    """

class IELMember(Interface):
    """Marker interface for .elmember.ELMember
    """

class IVenue(Interface):
    """Marker interface for .venue.Venue
    """

class IVenueFolder(Interface):
    """Marker interface for .venuefolder.VenueFolder
    """

##code-section FOOT
##/code-section FOOT