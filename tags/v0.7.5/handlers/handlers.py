import transaction
import logging

from Products.CMFCore.utils import getToolByName

logger = logging.getLogger('Events Handlers')

def signupCreated(obj, event):
    """ Someone registered for an event
    """
    if obj.portal_type != 'Booking':
        return

    mt = getToolByName(obj, 'portal_membership')
    member = mt.getAuthenticatedMember()

    # set the default values of the event preferences
    # home = mt.getHomeFolder(member.getId())
    if 'event_attendance' in member.objectIds():
        attendance_prefs = member['event_attendance']
        if attendance_prefs.getInitials() != obj.getInitials():
            attendance_prefs.setInitials(obj.getInitials())
        if attendance_prefs.getTelephone() != obj.getPhone():
            attendance_prefs.setTelephone(obj.getPhone())
        if attendance_prefs.getMobile() != obj.getMobile():
            attendance_prefs.setMobile(obj.getMobile())
        if attendance_prefs.getIceNumber() != obj.getIceNumber():
            attendance_prefs.setIceNumber(obj.getIceNumber())
        if attendance_prefs.getFax() != obj.getFax():
            attendance_prefs.setFax(obj.getFax())
        if attendance_prefs.getCompany() != obj.getCompany():
            attendance_prefs.setCompany(obj.getCompany())
        if attendance_prefs.getJobTitle() != obj.getFunction():
            attendance_prefs.setJobTitle(obj.getFunction())
        if attendance_prefs.getMealPreference() != obj.getMealPreference():
            attendance_prefs.setMealPreference(obj.getMealPreference())
        if attendance_prefs.getOtherMealPreference() != obj.getOtherMealPreference():
            attendance_prefs.setOtherMealPreference(obj.getOtherMealPreference())
        if attendance_prefs.getCountry() != obj.getCountry():
            attendance_prefs.setCountry(obj.getCountry())

    logger.info('Booking object initialized')

    # send an email to the attendee
    mailhost = getToolByName(obj, 'MailHost')
    attendee_name = '%s %s %s' % \
            (obj.getSalutation(), obj.getFirstname(), obj.getSurname())
    attendee_email = obj.getEmail()
    pu = getToolByName(obj, 'portal_url')
    portal = pu.getPortalObject()
    sender_email = portal['email_from_address']
    attendee_msg = """Dear %s

Thankyou for registering for the '%s' event. 

Visit the link below to view the details of your booking, as well as the cost involved.

%s/view

Kind regards,
The EventsList Team
    """ % (attendee_name, obj.Title(), obj.absolute_url())
    mailhost.send(attendee_msg, mto=attendee_email, mfrom=sender_email, 
                  subject='Event Attendance Request', encode=None)

    # send an email to the organiser
    event = obj.getElevents()
    organiser_name = event.contact_name()
    organiser_email = event.contact_email()
    organiser_msg = """Dear %s

This is a notification that %s has registered to attend the '%s' event.

Click the link below to view the event registration screen page and accept or reject the registration.

%s

Kind regards,
The EventsList Team
    """ % (organiser_name, attendee_name, obj.Title(), '%s/events_folder' % pu())
    #logger.info('Send email from %s to %s' % (
    #    organiser_email, sender_email))
    mailhost.send(organiser_msg, mto=organiser_email, mfrom=sender_email, 
                  subject='Event Attendance Request', encode=None)

    logger.info('Email sent to attendee and organiser')



def bookingTransition(obj, notification):
    """ handle a transition on a booking
    """
    if obj.portal_type != 'Booking':
        return

    if notification.status['review_state'] == 'submitted':
        return

    # send an email to the attendee
    mailhost = getToolByName(obj, 'MailHost')
    attendee_name = '%s %s %s' % \
            (obj.getSalutation(), obj.getFirstname(), obj.getSurname())
    attendee_email = obj.getEmail()
    pu = getToolByName(obj, 'portal_url')
    portal = pu.getPortalObject()
    sender_email = portal['email_from_address']
    attendee_msg = """Dear %s

This is a note to inform you that the status of your registration for the '%s' event is now '%s'.

Visit the link below to view the details of your booking, as well as the cost involved.

%s/view

Kind regards,
The EventsList Team
    """ % (attendee_name, obj.Title(), notification.new_state.title, obj.absolute_url())
    mailhost.send(attendee_msg, mto=attendee_email, mfrom=sender_email, 
                  subject='Event Attendance Notification', encode=None)

    logger.info('Status change Email sent to attendee')
